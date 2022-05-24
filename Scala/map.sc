class Pair(private val m_key : Any, private var m_value : Any) {
  def key() : Any = {
    m_key
  }

  def value() : Any = {
    m_value
  }

  def setValue(value : Any) = {
    m_value = value
  }

  override def toString() : String = {
    s"(${m_key}, ${m_value})"
  }
}

class Cell(private val m_pair: Pair, private var m_next : Cell) {
  def pair() : Pair = {
    m_pair
  }

  def next() : Cell = {
    m_next
  }

  def setNext(next : Cell) = {
    m_next = next
  }

  override def toString() : String = {
    m_pair.toString()
  }
}

class MyMap {
  private var m_first : Cell = null
  private var m_last : Cell = null
  private var m_size : Int = 0

  def put(key : Any, value : Any) : Any = {
    putX(m_first, key, value, null)
  }

  private def putX(current : Cell, key : Any, value : Any, last : Cell) : Any = {
    if (current != null) {
      if (key == current.pair().key()) {
        val previousvalue = current.pair().value()
        current.pair().setValue(value)
        previousvalue
      }
      else {
        putX(current.next(), key, value, current)
      }
    }
    else {
      if (last != null) {
        last.setNext(Cell(Pair(key, value), null))
      }
      else {
        m_first = Cell(Pair(key, value), null)
        m_last = m_first
      }

      m_size = m_size + 1
    }
  }

  def exists(key : Any) : Boolean = {
    existsX(m_first, key, null)
  }

  private def existsX(current : Cell, key : Any, last : Cell) : Boolean = {
    if (current != null) {
      if (key == current.pair().key()) {
        true
      }
      else {
        existsX(current.next(), key, current)
      }
    }
    else {
      false
    }
  }

  def remove(key : Any) : Any = {
    removeX(m_first, key, null)
  }

  private def removeX(current : Cell, key : Any, last : Cell) : Any = {
    if (current != null) {
      if (key == current.pair().key()) {
        val previousvalue = current.pair().value()

        if (last != null) {
          last.setNext(current.next())
        }
        else {
          m_first = m_first.next()
        }

        m_size = m_size - 1
        previousvalue
      }
      else {
        removeX(current.next(), key, current)
      }
    }
    else {
      null
    }
  }

  def size() : Int = {
    m_size
  }

  override def toString() : String = {
    s"[${toStringX(m_first, true)}]"
  }

  private def toStringX(current : Cell, first : Boolean) : String = {
    if (current != null) {
      (if (first) "" else ",") + current.toString() + toStringX(current.next(), false)
    }
    else {
      ""
    }
  }
}

object Main extends App {
  var m = MyMap()
  println(m)
  println(s"Size: ${m.size()}")
  println()

  m.put(1, "A")
  println(m)
  println(s"Size: ${m.size()}")
  println()

  m.put(2, "B")
  println(m)
  println(s"Size: ${m.size()}")
  println()

  m.put(3, "C")
  println(m)
  println(s"Size: ${m.size()}")
  println()

  m.put(2, "D")
  println(m)
  println(s"Size: ${m.size()}")
  println()
  
  println(s"Exists(0): ${m.exists(0)}")
  println(s"Exists(1): ${m.exists(1)}")
  println(s"Exists(2): ${m.exists(2)}")
  println(s"Exists(3): ${m.exists(3)}")
  println(s"Exists(4): ${m.exists(4)}")
  println()

  println(s"Remove 2: ${m.remove(2)}")
  println(m)
  println(s"Size: ${m.size()}")
  println()
  
  println(s"Remove 0: ${m.remove(0)}")
  println(m)
  println(s"Size: ${m.size()}")
  println()

  println(s"Remove 1: ${m.remove(1)}")
  println(m)
  println(s"Size: ${m.size()}")
  println()
  
  println(s"Remove 3: ${m.remove(3)}")
  println(m)
  println(s"Size: ${m.size()}")
}