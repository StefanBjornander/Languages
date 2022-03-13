// Stefan Björnander

#include <fstream>
#include <cassert>
using namespace std;

#include "Index.h"

Index::Index(void)
 :m_bitsPerIndex(0),
  m_index(0) {
  // Empty.
}

Index::Index(int bitsPerIndex, int index)
 :m_bitsPerIndex(bitsPerIndex),
  m_index(index) {
  // Empty.
}

Index::Index(const Index& index)
 :m_bitsPerIndex(index.m_bitsPerIndex),
  m_index(index.m_index) {
  // Empty.
}

Index& Index::operator=(const Index& index) {
  m_bitsPerIndex = index.m_bitsPerIndex;
  m_index = index.m_index;
  return *this;
}

bool Index::operator==(const Index& index) const {
  assert(m_bitsPerIndex == index.m_bitsPerIndex);
  return (m_index == index.m_index);
}

void Index::load(int bitsPerIndex, ifstream& inStream) {
  m_index = 0;
  m_bitsPerIndex = bitsPerIndex;
  inStream.read((char*) &m_index, m_bitsPerIndex / 8);
}

void Index::save(ofstream& outStream) const {
  outStream.write((char*) &m_index, m_bitsPerIndex / 8);
}
