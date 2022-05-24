class Pair:
  def __init__(self, key, value):
    self.__key = key;
    self.__value = value;
  def key(self):
    return self.__key;
  def value(self):
    return self.__value;
  def setKey(self, key):
    self.__key = key;
  def setValue(self, value):
    self.__value = value;
  def __str__(self):
    return "(" + self.__key.__str__() + "," + self.__value.__str__() + ")";

class Cell:
  def __init__(self, pair, next):
    super().__init__();
    self.__pair = pair;
    self.__next = next;
  def pair(self):
    return self.__pair;
  def next(self):
    return self.__next;
  def setValue(self, pair):
    self.__pair = pair;
  def setNext(self, next):
    self.__next = next;
  def __str__(self):
    return self.__pair.__str__();

class Map:
  def __init__(self):
    self.__first = None;
    self.__size = 0;
  def put(self, key, value):
    return self.putX(self.__first, key, value, None);
  def putX(self, current, key, value, last):
    if (current != None):
      if (key == current.pair().key()):
        previousValue = current.pair().value();
        current.pair().setValue(value);
        return previousValue;
      else:
        return self.putX(current.next(), key, value, current);
    else:
      if (last != None):
        last.setNext(Cell(Pair(key, value), None));
      else:
        self.__first = Cell(Pair(key, value), None);
      self.__size = self.__size + 1;
      return None;
  def exists(self, key):
    assert (self.__first != None), {'Map Empty'}
    return self.existsX(self.__first, key);
  def existsX(self, current, key):
    if (current != None):
      if (key == current.pair().key()):
        return True;
      else:
        return self.existsX(current.next(), key);
    else:
      return False;
  def remove(self, key):
    return self.removeX(self.__first, key, None);
  def removeX(self, current, key, last):
    if (current != None):
      if (key == current.pair().key()):
        previousValue = current.pair().value();
        if (last != None):
          last.setNext(current.next());
        else:
          self.__first = self.__first.next();
        self.__size = self.__size - 1;
        return previousValue;
      else:
        return self.removeX(current.next(), key, current);
    else:
      return None;
  def size(self):
    return self.__size;
  def __str__(self):
    return "[" + self.toString(self.__first, True) + "]";
  def toString(self, current, first):
    if (current):
      return ("" if first else ",") + current.pair().__str__() + self.toString(current.next(), False);
    else:
      return "";

m = Map();
print(m);
print("Size: " + str(m.size()));
print();

print("Put 1, A: " + str(m.put(1, 'A')));
print(m);
print("Size: " + str(m.size()));
print();

print("Put 2, B: " + str(m.put(2, 'B')));
print(m);
print("Size: " + str(m.size()));
print();

print("Put 3, C: " + str(m.put(3, 'C')));
print(m);
print("Size: " + str(m.size()));
print();

print("Put 2, D: " + str(m.put(2, 'D')));
print(m);
print("Size: " + str(m.size()));
print();

print("Exists 0: " + str(m.exists(0)));
print("Exists 1: " + str(m.exists(1)));
print("Exists 2: " + str(m.exists(2)));
print("Exists 3: " + str(m.exists(3)));
print("Exists 4: " + str(m.exists(4)));
print();

print("Remove 2: " + str(m.remove(2)));
print(m);
print("Size: " + str(m.size()));
print();

print("Remove 0: " + str(m.remove(0)));
print(m);
print("Size: " + str(m.size()));
print();

print("Remove 1: " + str(m.remove(1)));
print(m);
print("Size: " + str(m.size()));
print();

print("Remove 3: " + str(m.remove(3)));
print(m);
print("Size: " + str(m.size()));
