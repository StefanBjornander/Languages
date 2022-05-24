class Person {
  private var m_name : String

  constructor(name : String) {
    m_name = name
  }

  fun getName() : String {
    return m_name;
  }
}

fun main() {
  var p = Person("X")
  print(p.getName())
}