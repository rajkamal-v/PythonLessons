class MyClass:
  x = 5

p1 = MyClass()
print(p1.x)

class Person:
    def __init__(self, name, age): #constructor
        self.name = name
        self.age  = age

    def about_me(self):
        print("Hello My name is {}, and I am {}".format(self.name, self.age))

p1 = Person("John",36) #calls __init__  #p1 is the object

print(p1.name)
print(p1.age)

p1.about_me()

#modify object properties
p1.name = "Greg"
p1.about_me()

#deleting a property
del p1.age
#p1.about_me() # will produce AttributeError

#deleting object
del p1
