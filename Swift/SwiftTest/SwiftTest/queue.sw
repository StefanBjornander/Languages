class Cell : CustomStringConvertible {
  private var m_value : Any
  private var m_next : Cell?

  init(value : Any, next : Cell?) {
    m_value = value
    m_next = next
  }

  public var value : Any {
    get {
      return m_value
    }
    set {
      m_value = newValue
    }
  }

  public var next : Cell? {
    get {
      return m_next
    }
    set {
      m_next = newValue
    }
  }

  public var description : String {
    return String(describing: m_value)
  }
}

class Queue : CustomStringConvertible {
  private var m_first : Cell?
  private var m_last : Cell?
  private var m_size : Int

  init() {
    m_first = nil
    m_last = nil
    m_size = 0
  }

  public func add(value : Any) {
    if m_last != nil {
      m_last!.next = Cell(value: value, next: nil)
      m_last = m_last!.next
    }
    else {
      m_first = Cell(value: value, next: nil)
      m_last = m_first
    }

    m_size = m_size + 1
  }

  public func first() -> Any {
    assert(m_first != nil, "Empty Queue")
    return m_first!.value
  }

  public func remove() -> Any {
    assert(m_first != nil, "Empty Queue")
    let firstvalue = m_first!.value
    m_first = m_first!.next
    m_size = m_size - 1
    return firstvalue
  }

  public func size() -> Int {
    return m_size
  }

  public var description : String {
    return "[\(returnString(current: m_first, first: true))]"
  }

  private func returnString(current : Cell?, first : Bool) -> String {
    if current != nil {
      return (first ? "" : ",") + String(describing: current!.value) +
             returnString(current: current!.next, first: false)
    }
    else {
      return ""
    }      
  }
}

var q = Queue()
print(q)
print("Size: " + String(describing: q.size()))
print()

q.add(value: 1)
print(q)
print("Size: " + String(describing: q.size()))
print()

q.add(value: 2)
print(q)
print("Size: " + String(describing: q.size()))
print()

q.add(value: 3)
print(q)
print("Size: " + String(describing: q.size()))
print()

print("First: " + String(describing: q.first()))
print("Remove: " + String(describing: q.remove()))
print(q)
print("Size: " + String(describing: q.size()))
print()

print("First: " + String(describing: q.first()))
print("Remove: " + String(describing: q.remove()))
print(q)
print("Size: " + String(describing: q.size()))
print()

print("First: " + String(describing: q.first()))
print("Remove: " + String(describing: q.remove()))
print(q)