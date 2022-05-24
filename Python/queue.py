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

class Queue:
  def __init__(self):
    self.__first = None;
    self.__last = None;
    self.__size = 0;
  def add(self, value):
    if (self.__first == None):
      self.__first = self.__last = Cell(value, None);
    else:
      self.__last.setNext(Cell(value, None));
      self.__last = self.__last.next();
    self.__size = self.__size + 1;
  def first(self):
    assert (self.__first != None), {'Queue Empty'}
    return self.__first.value();
  def remove(self):
    assert (self.__first != None), {'Queue Empty'}
    firstvalue = self.__first.value();
    self.__first = self.__first.next();
    if (self.__first == None):
      self.__last = None;
    self.__size = self.__size - 1;
    return firstvalue;
  def size(self):
    return self.__size;
  def __str__(self):
    return "[" + self.toString(self.__first, True) + "]";
  def toString(self, current, first):
    if (current):
      return ("" if first else ",") + current.value().__str__() + self.toString(current.next(), False);
    else:
      return "";

q = Queue();
print(q);
print("Size: " + str(q.size()));
print();

q.add(1);
print(q);
print("First: " + str(q.first()));
print("Size: " + str(q.size()));
print();

q.add(2);
print(q);
print("First: " + str(q.first()));
print("Size: " + str(q.size()));
print();

q.add(3);
print(q);
print("First: " + str(q.first()));
print("Size: " + str(q.size()));
print();

print("Remove: " + str(q.remove()));
print(q);
print("First: " + str(q.first()));
print("Size: " + str(q.size()));
print();

print("Remove: " + str(q.remove()));
print(q);
print("First: " + str(q.first()));
print("Size: " + str(q.size()));
print();

print("Remove: " + str(q.remove()));
print(q);
print("Size: " + str(q.size()));