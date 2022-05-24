class Person:
  def __init__(self, name):
    super().__init__();
    self.name = name;
  def __str__(self):
    return super().__str__() + f" Person {self.name}";

class Student(Person):
  def __init__(self, name, university):
    super().__init__(name);
    self.university = university;
  def __str__(self):
    return super().__str__() + f" Student {self.university}";

class Employee(Person):
  def __init__(self, name, company):
    super().__init__(name);
    self.company = company;
  def __str__(self):
    return super().__str__() + f" Employee {self.company}";

p = Person("Adam");
s = Student("Bertil", "Umea");
e = Employee("Ceasar", "Volvo");

print(p);
print(s);
print(e);




