class Cell(m_value: Any, m_next : Cell) {
  def value() : Any = {
    m_value
  }

  def next() : Cell = {
    m_next
  }

  override def toString() : String = {
    m_value.toString()
  }
}

class Stack {
  var m_first : Cell = null
  var m_size : Int = 0

  def push(value : Any) = {
    m_first = Cell(value, m_first)
    m_size = m_size + 1
  }

  def top() : Any = {
    assert(m_first != null)
    m_first.value()
  }

  def pop() : Any = {
    assert(m_first != null)
    val firstvalue : Any= m_first.value()
    m_first = m_first.next()
    m_size = m_size - 1
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
  var s = Stack()
  println(s)
  println(s"Size: ${s.size()}")
  println()

  s.push(1)
  println(s)
  println(s"Top: ${s.top()}")
  println(s"Size: ${s.size()}")
  println()

  s.push(2)
  println(s)
  println(s"Top: ${s.top()}")
  println(s"Size: ${s.size()}")
  println()

  s.push(3)
  println(s)
  println(s"Top: ${s.top()}")
  println(s"Size: ${s.size()}")
  println()
  
  println(s"Pop: ${s.pop()}")
  println(s)
  println(s"Top: ${s.top()}")
  println(s"Size: ${s.size()}")
  println()
  
  println(s"Pop: ${s.pop()}")
  println(s)
  println(s"Top: ${s.top()}")
  println(s"Size: ${s.size()}")
  println()
  
  println(s"Pop: ${s.pop()}")
  println(s)
  println(s"Size: ${s.size()}")
}