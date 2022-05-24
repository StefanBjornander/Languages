class Pair : CustomStringConvertible {
  private var m_key : Int
  private var m_value : String

  init(key: Int, value: String) {
    m_key = key
    m_value = value
  }

  public var key : Int {
    get {
      return m_key
    }
    set {
      m_key = newValue
    }
  }

  public var value : String {
    get {
      return m_value
    }
    set {
      m_value = newValue
    }
  }

  public var description : String {
    return "(\(String(describing: m_key)),\(String(describing: m_value)))"
  }
}

class Cell : CustomStringConvertible {
  private var m_pair : Pair
  private var m_next : Cell?

  init(pair : Pair, next : Cell?) {
    m_pair = pair
    m_next = next
  }

  public var pair : Pair {
    get {
      return m_pair
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
    return String(describing: m_pair)
  }
}

class Map : CustomStringConvertible {
  private var m_first : Cell?
  private var m_size : Int

  init() {
    m_first = nil
    m_size = 0
  }

  public func put(key: Int, value: String) -> String? {
    return putX(current: m_first, key: key, value: value, last: nil)
  }

  private func putX(current: Cell?, key: Int, value: String, last: Cell?) -> String? {
    if current != nil {
      if key == current!.pair.key {
        let previousvalue = current!.pair.value
        current!.pair.value = value
        return previousvalue
      }
      else {
        return putX(current: current!.next, key: key, value: value, last: current)
      }
    }
    else {
      if last != nil {
        last!.next = Cell(pair: Pair(key: key, value: value), next: nil)
      }
      else {
        m_first = Cell(pair: Pair(key: key, value: value), next: nil)
      }

      m_size = m_size + 1
      return nil
    }
  }

  public func exists(key: Int) -> Bool {
    return existsX(current: m_first, key: key)
  }

  private func existsX(current: Cell?, key: Int) -> Bool {
    if current != nil {
      if key == current!.pair.key {
        return true
      }
      else {
        return existsX(current: current!.next, key: key)
      }
    }
    else {
      return false
    }
  }

  public func remove(key: Int) -> String? {
    return removeX(current: m_first, key: key, last: nil)
  }

  private func removeX(current: Cell?, key: Int, last: Cell?) -> String? {
    if current != nil {
      if key == current!.pair.key {
        let previousvalue = current!.pair.value

        if last != nil {
          last!.next = current!.next
        }
        else {
          m_first = m_first!.next
        }

        m_size = m_size - 1
        return previousvalue
      }
      else {
        return removeX(current: current!.next, key: key, last: current)
      }
    }
    else {
      return nil
    }
  }

  public func size() -> Int {
    return m_size
  }

  public var description : String {
    return "[\(returnString(current: m_first, first: true))]"
  }

  private func returnString(current: Cell?, first: Bool) -> String {
    if current != nil {
      return (first ? "" : ",") + String(describing: current!.pair) +
             returnString(current: current!.next, first: false)
    }
    else {
      return ""
    }      
  }
}

var m = Map()
print(m)
print("Size: " + String(describing: m.size()))
print()

print("Put 1 A: " + (m.put(key: 1, value: "A") ?? "nil"))
print(m)
print("Size: " + String(describing: m.size()))
print()

print("Put 2 B: " + (m.put(key: 2, value: "B") ?? "nil"))
print(m)
print("Size: " + String(describing: m.size()))
print()

print("Put 3 C: " + (m.put(key: 3, value: "C") ?? "nil"))
print(m)
print("Size: " + String(describing: m.size()))
print()

print("Put 2 D: " + (m.put(key: 2, value: "D") ?? "nil"))
print(m)
print("Size: " + String(describing: m.size()))
print()

print("Exists 0: " + String(m.exists(key: 0)))
print("Exists 1: " + String(m.exists(key: 1)))
print("Exists 2: " + String(m.exists(key: 2)))
print("Exists 3: " + String(m.exists(key: 3)))
print("Exists 4: " + String(m.exists(key: 4)))
print()

print("Remove: " + (m.remove(key: 2) ?? "nil"))
print(m)
print("Size: " + String(describing: m.size()))
print()

print("Remove: " + (m.remove(key: 2) ?? "nil"))
print(m)
print("Size: " + String(describing: m.size()))
print()

print("Remove: " + (m.remove(key: 1) ?? "nil"))
print(m)
print("Size: " + String(describing: m.size()))
print()

print("Remove: " + (m.remove(key: 3) ?? "nil"))
print(m)
print("Size: " + String(describing: m.size()))
