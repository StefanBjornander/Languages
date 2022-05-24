class Person(name : String) {
  override def toString() : String = {
    s"Person ${name}"
  }
}

class Student(name : String, university : String) extends Person(name) {
  override def toString() : String = {
    s"${super.toString()} Student ${university}"
  }
}

 class Employee(name : String, company : String) extends Person(name) {
  override def toString() : String = {
    s"${super.toString()} Employee ${company}"
  }
}

object Main extends App {
  var p = Person("Adam")
  println(p)
  var s = Student("Bertil", "Umea")
  println(s)
  var e = Employee("Ceaser", "Volvo")
  println(e)
}