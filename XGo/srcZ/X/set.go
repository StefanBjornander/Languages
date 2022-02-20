package set

type Stringable interface {
  String() string 
}

type Cell struct {
  m_next *Cell
  m_value interface{}
}

type Set struct {
  m_size int
  m_first *Cell
}

type Iterator struct {
  m_link *Cell
}

func New() *Set {
  setPtr := new(Set)
  setPtr.m_size = 0
  setPtr.m_first = nil
  return setPtr
}

func (setPtr *Set) Size() int {
  return setPtr.m_size
}

func (setPtr *Set) Add(value interface{}) bool {
  for currLink := setPtr.m_first; currLink != nil; currLink = currLink.m_next {
    if value == currLink.m_value {
      return false
    }
  }
  
  newCellPtr := new(Cell)
  newCellPtr.m_next = setPtr.m_first
  newCellPtr.m_value = value
  setPtr.m_first = newCellPtr
  setPtr.m_size++
  return true
}

func (setPtr *Set) Remove(value interface{}) bool {
  var prevLink *Cell = nil

  for currLink := setPtr.m_first; currLink != nil; currLink = currLink.m_next {
    if value == currLink.m_value {
      if prevLink != nil {
        prevLink.m_next = currLink.m_next
      } else {
        setPtr.m_first = currLink.m_next
      }

      setPtr.m_size--
      return true
    }

    prevLink = currLink
  }

  return false
}

func (setPtr *Set) Contains(value interface{}) bool {
  for currLink := setPtr.m_first; currLink != nil; currLink = currLink.m_next {
    if value == currLink.m_value {
      return true
    }
  }
  
  return false
}

func (setPtr *Set) Front() *Iterator {
  if setPtr.m_first == nil {
    return nil
  } else {
    iteratorPtr := new(Iterator)
    iteratorPtr.m_link = setPtr.m_first
    return iteratorPtr
  }
}

func (iteratorPtr *Iterator) Next() *Iterator {
  if iteratorPtr.m_link.m_next == nil {
    return nil
  } else {
    iteratorPtr.m_link = iteratorPtr.m_link.m_next
    return iteratorPtr
  }
}

func (iteratorPtr *Iterator) Value() interface{} {
  return iteratorPtr.m_link.m_value
}