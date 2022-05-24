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

class Stack : CustomStringConvertible {
  private var m_first : Cell?
  private var m_size : Int

  init() {
    m_first = nil
    m_size = 0
  }

  public func push(value : Any) {
    m_first = Cell(value: value, next: m_first)
    m_size = m_size + 1
  }

  public func top() -> Any {
    assert(m_first != nil, "Empty Stack")
    return m_first!.value
  }

  public func pop() -> Any {
    assert(m_first != nil, "Empty Stack")
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

var s = Stack()
print(s)
print("Size: " + String(describing: s.size()))
print()

s.push(value: 1)
print(s)
print("Size: " + String(describing: s.size()))
print()

s.push(value: 2)
print(s)
print("Size: " + String(describing: s.size()))
print()

s.push(value: 3)
print(s)
print("Size: " + String(describing: s.size()))
print()

print("Top: " + String(describing: s.top()))
print("Pop: " + String(describing: s.pop()))
print(s)
print("Size: " + String(describing: s.size()))
print()

print("Top: " + String(describing: s.top()))
print("Pop: " + String(describing: s.pop()))
print(s)
print("Size: " + String(describing: s.size()))
print()

print("Top: " + String(describing: s.top()))
print("Pop: " + String(describing: s.pop()))
print(s)
print("Size: " + String(describing: s.size()))
