class Person 
  String :m_name

  def initialize name:
    @m_name = name
  end

  public def to_s
    "Person #{@m_name}"
  end
end

class Student < Person
  String :m_university

  def initialize name:, university:
    super name: name
    @m_university = university
  end

  public def to_s
    "#{super} Student #{@m_university}"
  end
end

class Employee < Person
  String :m_company

  def initialize name:, company:
    super name: name
    @m_company = company
  end

  public def to_s
    "#{super} Employee #{@m_company}"
  end
end

p = Person.new name: "Adam"
puts p

s = Student.new name: "Bertil", university: "Umea"
puts s

e = Employee.new name: "Ceasar", company: "Volvo"
print e
