// Stefan Björnander

template <class Type>
class Block {
  public:
    Block();
    Block(int repetitions, const Type& value);

    int getRepetitions() const { return m_repetitions; }
    void setRepetitions(int repetitions) { m_repetitions = repetitions; }

    vector<Type>& valueList() {return m_valueList;}

  private:
    int m_repetitions;
    vector<Type> m_valueList;
};

template <class Type>
Block<Type>::Block()
  :m_repetitions(0) {
  // Empty.
}

template <class Type>
Block<Type>::Block(int repetitions, const Type& value)
  : m_repetitions(repetitions) {
  m_valueList.push_back(value);
}
