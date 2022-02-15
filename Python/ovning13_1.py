class Person:
    def __init__(self, name):
        self.name = name;

    def __str__(self):
        return f"Name: {self.name}";

class Student(Person):
    def __init__(self, name, school):
        super().__init__(name);
        self.school = school;

    def __str__(self):
        return super().__str__() + f", School: {self.school}";

p = Person("Adam");
print(p);

s = Student("Bertil", "High School");
print(s);

class Book:
    value = 123;

    @classmethod
    def getValue(cls):
        return cls.value;

    def __init__(self, author, title):
        self.__author = author;
        self.__title = title;

    def setAuthor(self, author):
        self.__author = author;

    def getAuthor(self):
        return self.__author;

    def setTitle(self, title):
        self.__title = title;

    def getTitle(self):
        return self.__title;

    def __str__(self):
        return f"Author: {self.author}, Title: {self.title}";

    def __eq__(self, other):
        return (type(self) == type(other)) and \
               (self.__author == other.__author) and \
               (self.title == other.title);

    author = property(getAuthor, setAuthor);
    title = property(getTitle, setTitle);

b = Book("Adam", "Test");
print(b.getAuthor(), b.getTitle());
b.setAuthor("Bertil");
b.setTitle("Hello");
print(b.getAuthor(), b.getTitle());

b.author = "Ceasar";
b.title = "Hi";
print(b.author, b.title);
print(b);

c = Book("Ceasar", "Hi");
print(b == c);
print(Book.value);
print(Book.getValue());
print(type(c));