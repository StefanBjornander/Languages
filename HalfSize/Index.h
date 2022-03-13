// Stefan Björnander

class Index {
  public:
    Index(void);
    Index(int bitsPerIndex, int index);
    Index(const Index& index);
    Index& operator=(const Index& index);

    int index() const {return m_index;}
    bool operator==(const Index& index) const;

    void load(int bitsPerIndex, ifstream& inStream);
    void save(ofstream& outStream) const;

  private:
    int m_bitsPerIndex, m_index;
};