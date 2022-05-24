class Cell:
  def __init__(self, value, next):
    super().__init__();
    self.__value = value;
    self.__next = next;
  def value(self):
    return self.__value;
  def next(self):
    return self.__next;
  def setValue(self, value):
    self.__value = value;
  def setNext(self, next):
    self.__next = next;
  def __str__(self):
    return "(" + self.__value.__str__() + "," + self.__next.__str__() + ")";

class Stack:
  def __init__(self):
    self.__first = None;
    self.__size = 0;
  def push(self, value):
    self.__first = Cell(value, self.__first);
    self.__size = self.__size + 1;
  def top(self):
    assert (self.__first != None), {'Stack Empty'}
    return self.__first.value();
  def pop(self):
    assert (self.__first != None), {'Stack Empty'}
    firstvalue = self.__first.value();
    self.__first = self.__first.next();
    self.__size = self.__size - 1;
    return firstvalue;
  def size(self):
    return self.__size;
  def __str__(self):
    return "[" + self.toString(self.__first, True) + "]";
  def toString(self, current, first):
    if current:
      return ("" if first else ",") + current.value().__str__() + self.toString(current.next(), False);
    else:
      return "";

s = Stack();
print(s);
print("Size: " + str(s.size()));
print();

s.push(1);
print(s);
print("Top: " + str(s.top()));
print("Size: " + str(s.size()));
print();

s.push(2);
print(s);
print("Top: " + str(s.top()));
print("Size: " + str(s.size()));
print();

s.push(3);
print(s);
print("Top: " + str(s.top()));
print("Size: " + str(s.size()));
print();

print("Pop: " + str(s.pop()));
print(s);
print("Top: " + str(s.top()));
print("Size: " + str(s.size()));
print();

print("Pop: " + str(s.pop()));
print(s);
print("Top: " + str(s.top()));
print("Size: " + str(s.size()));
print();

print("Pop: " + str(s.pop()));
print(s);
print("Size: " + str(s.size()));