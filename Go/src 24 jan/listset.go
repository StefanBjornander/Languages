package listset

import "container/list"

/*type Stringable interface {
  String() string 
}*/

type Set struct {
  m_listPtr *list.List
}

type Iterator struct {
  m_listIteratorPtr *list.Element
  Value interface{}
}

func New() *Set {
  setPtr := new(Set);
  setPtr.m_listPtr = list.New();
  return setPtr
}

func (setPtr *Set) Size() int {
  return setPtr.m_listPtr.Len()
}

func (setPtr *Set) Add(value interface{}) bool {
  for iterator := setPtr.m_listPtr.Front(); iterator != nil; iterator = iterator.Next() {
    if value == iterator.Value {
      return false
    }
  }
  
  setPtr.m_listPtr.PushBack(value);
  return true
}

func (setPtr *Set) Remove(value interface{}) bool {
  for iterator := setPtr.m_listPtr.Front(); iterator != nil; iterator = iterator.Next() {
    if value == iterator.Value {
      setPtr.m_listPtr.Remove(iterator);
      return true
    }    
  }
  
  return false
}

func (setPtr *Set) Contains(value interface{}) bool {
  for iterator := setPtr.m_listPtr.Front(); iterator != nil; iterator = iterator.Next() {
    if value == iterator.Value {
      return true
    }    
  }
  
  return false
}

func (setPtr *Set) Front() *Iterator {
  listIteratorPtr := setPtr.m_listPtr.Front()

  if listIteratorPtr != nil {
    iteratorPtr := new(Iterator)
    iteratorPtr.m_listIteratorPtr = listIteratorPtr
    iteratorPtr.Value = listIteratorPtr.Value
    return iteratorPtr;
  } else {
    return nil
  }
}

func (iteratorPtr *Iterator) Next() *Iterator {
  listIteratorPtr := iteratorPtr.m_listIteratorPtr.Next();

  if listIteratorPtr != nil {
    iteratorPtr.m_listIteratorPtr = listIteratorPtr
    iteratorPtr.Value = listIteratorPtr.Value
    return iteratorPtr;
  } else {
    return nil;
  }
}