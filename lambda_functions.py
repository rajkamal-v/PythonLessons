#lambda - A lambda function is a small anonymous function.
#Syntax: lambda arguments:expression

x = lambda a: a*3
print(x(10)) #30

x = lambda a, b: a + b
print(x(3,5)) #8

def myfunc(n):
  return lambda a : a * n

'''the above function can be used to double or triple or quadraple etc.. '''

my_doubler = myfunc(2)
my_tripler = myfunc(3)

print(my_doubler(11)) #22
print(my_tripler(11)) #33
