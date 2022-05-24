/*func isEqual<T: Equatable>(type: T.Type, a: AnyObject, b: AnyObject) -> Bool {
  guard let a = a as? T, let b = b as? T else { return false }
  return a == b
}*/

class Person : CustomStringConvertible {
  private var m_name : String

  init(name : String) {
    m_name = name
  }

  public var description : String {
    return "Person \(m_name)"
  }
}

class Student : Person {
  private var m_university : String

  init(name : String, university : String) {
    m_university = university
    super.init(name: name)
  }

  public override var description : String {
    return "\(super.description) Student \(m_university)"
  }
}

class Employee : Person {
  private var m_company : String

  init(name : String, company : String) {
    m_company = company
    super.init(name: name)
  }

  public override var description : String {
    return "\(super.description) Employee \(m_company)"
  }
}

var p = Person(name: "Adam")
print(p)

var s = Student(name: "Bertil", university: "Umea")
print(s)

var e = Employee(name: "Ceasar", company: "Volvo")
print(e)
