#Inheritance allows us to define a class that inherits all the methods and properties from another class.
#Parent class
class Person:
  def __init__(self, fname, lname):
    self.firstname = fname
    self.lastname = lname

  def printname(self):
    print(self.firstname, self.lastname)

#Use the Person class to create an object, and then execute the printname method:

x = Person("John", "Doe")
x.printname()

#child class
class Student(Person): #student class inherits the properties and methods of Person class
    pass #pass is used if we dont want to define anything

x = Student("Greg", "House")
x.printname()


class Student(Person):
  def __init__(self, fname, lname, year):
    Person.__init__(self, fname, lname)
    self.graduationyear = year

  def welcome(self):
    print("Welcome", self.firstname, self.lastname, "to the class of", self.graduationyear)

x = Student("Mike", "Wilson", 1998)
x.printname()
x.welcome()
