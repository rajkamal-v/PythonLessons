
#program 1: IndentationError - when we forget to indent properly
'''
age = 36
if age > 36:
print('age is greater than 36') #IndentationError: expected an indented block
'''
#program 2: NameError - when an undefined variable name or incorrect variable name is used
'''
print(age) #NameError: name 'age' is not defined
'''

#program 3: AttributeError - when accessing deleted or undefined property/method of an object
'''
class Person:
  def __init__(self, name, age):
    self.name = name
    self.age = age

  def myfunc(self):
    print("Hello my name is " + self.name)

p1 = Person("John", 36)
del p1.name
p1.myfunc() #AttributeError - 'Person' object has no attribute 'name'
'''
