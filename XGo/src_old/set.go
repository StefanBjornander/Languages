package set

type Cell struct {
  m_nextLink *Cell
  m_value interface{}
}

type Set struct {
  m_size int
  m_firstLink *Cell
}

type Iterator struct {
  m_link *Cell
}

func New() *Set {
  setPtr := new(Set)
  setPtr.m_size = 0
  setPtr.m_firstLink = nil
  return setPtr
}

func (setPtr *Set) Size() int {
  return setPtr.m_size
}

func (setPtr *Set) Add(value interface{}) bool {
  if !setPtr.Contains(value) {
    newCellPtr := new(Cell)
    newCellPtr.m_nextLink = setPtr.m_firstLink
    newCellPtr.m_value = value
    setPtr.m_firstLink = newCellPtr
    setPtr.m_size++
    return true
  }

  return false
}

func (setPtr *Set) Remove(value interface{}) bool {
  var previousLink *Cell = nil

  for currentLink := setPtr.m_firstLink; currentLink != nil; currentLink = currentLink.m_nextLink {
    if value == currentLink.m_value {
      if currentLink == setPtr.m_firstLink {
        setPtr.m_firstLink = currentLink.m_nextLink
      } else {
        previousLink.m_nextLink = currentLink.m_nextLink
      }

      setPtr.m_size--
      return true
    }

    previousLink = currentLink
  }

  return false
}

func (setPtr *Set) Contains(value interface{}) bool {
  for link := setPtr.m_firstLink; link != nil; link = link.m_nextLink {
    if value == link.m_value {
      return true
    }
  }
  
  return false
}

/*func (setPtr *Set) Min() *Iterator {
  if setPtr.m_firstLink != nil {
    minValue := setPtr.m_firstLink.m_value
    minLink := setPtr.m_firstLink

    for link := setPtr.m_firstLink.m_nextLink; link != nil; link = link.m_nextLink {
      if link.m_value < minValue {
        minLink = link;
        minValue = link.m_value
      }
    }

    iteratorPtr := new(Iterator)
    iteratorPtr.m_link = minLink
    return iteratorPtr
  }

  return nil
}

func (setPtr *Set) Max() *Iterator {
  if setPtr.m_firstLink != nil {
    maxValue := setPtr.m_firstLink.m_value
    maxLink := setPtr.m_firstLink

    for link := setPtr.m_firstLink.m_nextLink; link != nil; link = link.m_nextLink {
      if link.m_value > maxValue {
        maxLink = link;
        maxValue = link.m_value
      }
    }

    iteratorPtr := new(Iterator)
    iteratorPtr.m_link = maxLink
    return iteratorPtr
  }

  return nil
}*/

func (setPtr *Set) Front() *Iterator {
  if setPtr.m_firstLink == nil {
    return nil
  } else {
    iteratorPtr := new(Iterator)
    iteratorPtr.m_link = setPtr.m_firstLink
    return iteratorPtr
  }
}

func (iteratorPtr *Iterator) Next() *Iterator {
  if iteratorPtr.m_link.m_nextLink == nil {
    return nil
  } else {
    iteratorPtr.m_link = iteratorPtr.m_link.m_nextLink
    return iteratorPtr
  }
}

func (iteratorPtr *Iterator) Value() interface{} {
  return iteratorPtr.m_link.m_value
}