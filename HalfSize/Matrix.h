// Stefan Björnander

template <class Type>
class Matrix {
  public:
    Matrix(int width, int height, bool compressed);
    ~Matrix();

    int width() const { return m_width; }
    int height() const { return m_height; }

    Type get(int row, int column) const;
    void set(int row, int column, const Type& value);

    void load(int numberOfBits, ifstream& inStream);
    void save(ofstream& outStream);

  private:
    int m_width, m_height;
    bool m_compressed;
    Type* m_buffer;
};

template <class Type>
Matrix<Type>::Matrix(int width, int height, bool compressed)
 :m_width(width),
  m_height(height),
  m_compressed(compressed) {
  assert((m_width > 0) && (m_height > 0));
  m_buffer = new Type[m_width * m_height];
  assert(m_buffer != nullptr);
}

template <class Type>
Matrix<Type>::~Matrix() {
  delete [] m_buffer;
}

template <class Type>
Type Matrix<Type>::get(int row, int column) const {
  return m_buffer[(row * m_width) + column];
}

template <class Type>
void Matrix<Type>::set(int row, int column, const Type& value) {
  m_buffer[(row * m_width) + column] = value;
}

template <class Type>
void Matrix<Type>::load(int numberOfBits, ifstream& inStream) {
  if (!m_compressed) {
    for (int row = 0; row < m_height; ++row) {
      for (int column = 0; column < m_width; ++column) {
        Type value;
        value.load(numberOfBits, inStream);
        set(row, column, value);
      }
    }
  }
  else {
    int size = m_width * m_height, index = 0;

    while (index < size) {
      char repetitionCount;
      inStream.read(&repetitionCount, sizeof repetitionCount);

      bool runLength = ((repetitionCount & 0x80) != 0);
      int repetitions = ((int) (repetitionCount & 0x7F)) + 1;

      if (runLength) {
        Type value;
        value.load(numberOfBits, inStream);

        for (int count = 0; count < repetitions; ++count) {
          int row = index / m_width, column = index % m_width;
          set(row, column, value);
          ++index;
        }
      }
      else {
        for (int count = 0; count < repetitions; ++count) {
          Type value;
          value.load(numberOfBits, inStream);
          int row = index / m_width, column = index % m_width;
          set(row, column, value);
          ++index;
        }
      }
    }
  }
}

template <class Type>
void Matrix<Type>::save(ofstream& outStream) {
  if (!m_compressed) {
    for (int row = 0; row < m_height; ++row) {
      for (int column = 0; column < m_width; ++column) {
        get(row, column).save(outStream);
      }
    }
  }
  else {
    for (int row = 0; row < m_height; ++row) {
      vector<Block<Type>> blockList;
      Type currValue = get(row, 0);
      int currColumn = 0;

      for (int column = 1; column < m_width; ++column) {
        Type value = get(row, column);

        if (!(value == currValue)) {
          blockList.push_back(Block<Type>(column - currColumn, currValue));
          currValue = value;
          currColumn = column;
        }
      }

      if (currColumn < m_width) {
        blockList.push_back(Block<Type>(m_width - currColumn, currValue));
      }

      vector<pair<int,int>> pairList;
	  int currIndex = ((int) blockList.size()) - 1;
	  int lastOneIndex = -1;

      vector<Block<Type>> newBlockList;
      Block<Type> rawBlock;

      for (Block<Type>& block : blockList) {
        if (block.getRepetitions() == 1) {
          rawBlock.setRepetitions(rawBlock.getRepetitions() + 1);
          rawBlock.valueList().push_back(block.valueList().front());
        }
        else {
          if (rawBlock.getRepetitions() > 0) {
            newBlockList.push_back(rawBlock);
            rawBlock = Block<Type>();
          }

          newBlockList.push_back(block);
        }
      }

      if (rawBlock.getRepetitions() > 0) {
        newBlockList.push_back(rawBlock);
      }

      for (Block<Type>& block : newBlockList) {
        if ((block.getRepetitions() > 1) &&
            (block.valueList().size() == 1)) {
          char repetitionCount =
            0x80 | (0x7F & (block.getRepetitions() - 1));
          outStream.write((char*) &repetitionCount,
                          sizeof repetitionCount);
          Type value = block.valueList().front();
          value.save(outStream);
        }
        else {
          assert(block.getRepetitions() == block.valueList().size());
          char repetitionCount =
            0x7F & (block.getRepetitions() - 1);
          outStream.write(&repetitionCount, sizeof repetitionCount);

          for (const Type& value : block.valueList()) {
            value.save(outStream);
          }
        }
      }
    }
  }
}
