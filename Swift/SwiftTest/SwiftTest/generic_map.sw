class Pair<KeyType : Equatable,ValueType> {
  private var m_key : KeyType
  private var m_value : ValueType

  init(key : KeyType, value : ValueType) {
    m_key = key
    m_value = value
  }

  public var key : KeyType {
    get {
      return m_key
    }
    set {
      m_key = newValue
    }
  }

  public var value : ValueType {
    get {
      return m_value
    }
    set {
      m_value = newValue
    }
  }

  public func toString() -> String {
    return "(\(m_key),\(m_value))"
  }

  public var description : String {
    return "(\(m_key)),\(m_value)))"
  }
}

class Cell<KeyType : Equatable,ValueType> : CustomStringConvertible {
  private var m_pair : Pair<KeyType,ValueType>
  private var m_next : Cell<KeyType,ValueType>?

  init(pair : Pair<KeyType,ValueType>, next : Cell<KeyType,ValueType>?) {
    m_pair = pair
    m_next = next
  }

  public var pair : Pair<KeyType,ValueType> {
    get {
      return m_pair
    }
  }

  public var next : Cell<KeyType,ValueType>? {
    get {
      return m_next
    }
    set {
      m_next = newValue
    }
  }

  public func toString() -> String {
    return m_pair.toString()
  }

  public var description : String {
    return "\(m_pair)"
  }
}

class Map<KeyType : Equatable,ValueType> : CustomStringConvertible {
  private var m_first : Cell<KeyType,ValueType>?
  private var m_size : Int

  init() {
    m_first = nil
    m_size = 0
  }

  public func put(key : KeyType, value : ValueType) -> ValueType? {
    return putX(current : m_first, key : key, value : value, last : nil)
  }

  private func putX(current : Cell<KeyType,ValueType>?, key : KeyType, value : ValueType,
                    last : Cell<KeyType,ValueType>?) -> ValueType? {
    if current != nil {
      if key == current!.pair.key {
        let previousvalue = current!.pair.value
        current!.pair.value = value
        return previousvalue
      }
      else {
        return putX(current : current!.next, key : key, value : value, last : current)
      }
    }
    else {
      if last != nil {
        last!.next = Cell<KeyType,ValueType>(pair : Pair<KeyType,ValueType>(key : key, value : value),
                                             next : nil)
      }
      else {
        m_first = Cell<KeyType,ValueType>(pair : Pair<KeyType,ValueType>(key : key, value : value),
                                          next : nil)
      }

      m_size = m_size + 1
      return nil
    }
  }

  public func exists(key : KeyType) -> Bool {
    return existsX(current : m_first, key : key)
  }

  private func existsX(current : Cell<KeyType,ValueType>?, key : KeyType) -> Bool {
    if current != nil {
      if key == current!.pair.key {
        return true
      }
      else {
        return existsX(current : current!.next, key : key)
      }
    }
    else {
      return false
    }
  }

  public func remove(key : KeyType) -> ValueType? {
    return removeX(current : m_first, key : key, last : nil)
  }

  private func removeX(current : Cell<KeyType,ValueType>?, key : KeyType,
                       last : Cell<KeyType,ValueType>?) -> ValueType? {
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
        return removeX(current : current!.next, key : key, last : current)
      }
    }
    else {
      return nil
    }
  }

  public func size() -> Int {
    return m_size
  }

  public func toString() -> String {
    return "[\(returnString(current : m_first, first : true))]"
  }

  public var description : String {
    return "[\(returnString(current : m_first, first : true))]"
  }

  private func returnString(current : Cell<KeyType,ValueType>?, first : Bool) -> String {
    if current != nil {
      return (first ? "" : ",") + current!.pair.toString() +
             returnString(current : current!.next, first : false)
    }
    else {
      return ""
    }      
  }
}

var m = Map<Int,String>()
print(m.toString())
print("Size : " + String(describing : m.size()))
print()

print("Put 1 A: " + (m.put(key : 1, value : "A") ?? "nil"))
print(m.toString())
print("Size : " + String(describing : m.size()))
print()

print("Put 2 B: " + (m.put(key : 2, value : "B") ?? "nil"))
print(m.toString())
print("Size : " + String(describing : m.size()))
print()

print("Put 3 C: " + (m.put(key : 3, value : "C") ?? "nil"))
print(m.toString())
print("Size : " + String(describing : m.size()))
print()

print("Put 2 D: " + (m.put(key : 2, value : "D") ?? "nil"))
print(m.toString())
print("Size : " + String(describing : m.size()))
print()

print("Exists 0: " + String(m.exists(key : 0)))
print("Exists 1: " + String(m.exists(key : 1)))
print("Exists 2: " + String(m.exists(key : 2)))
print("Exists 3: " + String(m.exists(key : 3)))
print("Exists 4: " + String(m.exists(key : 4)))
print()

print("Remove : " + (m.remove(key : 2) ?? "nil"))
print(m.toString())
print("Size : " + String(describing : m.size()))
print()

print("Remove : " + (m.remove(key : 2) ?? "nil"))
print(m.toString())
print("Size : " + String(describing : m.size()))
print()

print("Remove : " + (m.remove(key : 1) ?? "nil"))
print(m.toString())
print("Size : " + String(describing : m.size()))
print()

print("Remove : " + (m.remove(key : 3) ?? "nil"))
print(m.toString())
print("Size : " + String(describing : m.size()))
