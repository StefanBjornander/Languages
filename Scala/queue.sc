class Cell(val m_value: Any, var m_next : Cell) {
  def value() : Any = {
    m_value
  }

  def next() : Cell = {
    m_next
  }

  def setNext(next : Cell) = {
    m_next = next
  }

  override def toString() : String = {
    m_value.toString()
  }
}

class Queue {
  var m_first : Cell = null
  var m_last : Cell = null
  var m_size : Int = 0

  def add(value : Any) = {
    if (m_first != null) {
      m_last.setNext(Cell(value, null))
      m_last = m_last.next()
    }
    else {
      m_first = Cell(value, null)
      m_last = m_first
    }

    m_size = m_size + 1
  }

  def first() : Any = {
    assert(m_first != null)
    m_first.value()
  }

  def remove() : Any = {
    assert(m_first != null)
    val firstvalue : Any= m_first.value()
    m_first = m_first.next()
    firstvalue
  }

  def size() : Int = {
    m_size
  }

  override def toString() : String = {
    s"[${toStringX(m_first, true)}]"
  }

  def toStringX(current : Cell, first : Boolean) : String = {
    if (current != null) {
      (if (first) "" else ",") + current.toString() + toStringX(current.next(), false)
    }
    else {
      ""
    }
  }
}

object Main extends App {
  var s = Queue()
  println(s)
  println(s"Size: ${s.size()}")
  println()

  s.add(1)
  println(s)
  println(s"First: ${s.first()}")
  println(s"Size: ${s.size()}")
  println()

  s.add(2)
  println(s)
  println(s"First: ${s.first()}")
  println(s"Size: ${s.size()}")
  println()

  s.add(3)
  println(s)
  println(s"First: ${s.first()}")
  println(s"Size: ${s.size()}")
  println()
  
  println(s"Remove: ${s.remove()}")
  println(s)
  println(s"First: ${s.first()}")
  println(s"Size: ${s.size()}")
  println()
  
  println(s"Remove: ${s.remove()}")
  println(s)
  println(s"First: ${s.first()}")
  println(s"Size: ${s.size()}")
  println()
  
  println(s"Remove: ${s.remove()}")
  println(s)
  println(s"Size: ${s.size()}")
}