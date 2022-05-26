Person = {}

Person.new = function(self, object)
  object = object or {}
  setmetatable(object, self)
  self.__index = self
  return object
end

Person.construct = function(self, n)
  return Person.new(self, {name = n})
end

Person.__tostring = function(self)
  return "Person " .. self.name
end

Student = Person:new()

Student.construct = function(self, n, u)
  s = Person.construct(self, n)
  s.university = u
  return s
end

Student.__tostring = function(self)
  return Person.__tostring(self) ..
         " Student " .. self.university
end

Employee = Person:new()

Employee.construct = function(self, n, c)
  s = Person.construct(self, n)
  s.company = c
  return s
end

Employee.__tostring = function(self)
  return Person.__tostring(self) ..
         " Employee " .. self.company
end

p = Person:construct("Adam")
print(p)

s = Student:construct("Bertil", "Umea")
print(s)

e = Employee:construct("Bertil", "Volvo")
print(e)
