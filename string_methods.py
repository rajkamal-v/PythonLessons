my_string = "Hello, Python"

print(my_string.split(',')) # will split and return a list of strings ['Hello',' Python']
print(my_string.lower())    # returns the string in lower case
print(my_string.upper())    # returns the string in upper case
print(my_string.replace('o','0')) # replace the mentioned character with given character
print(my_string[0]) # a string is a character array, so we can access each chacracter by their index
print(my_string[2:5]) #Substring. Get the characters from position 2 to position 5 (not included)

my_another_string = '  string_with_space  '

print(my_another_string.strip()) #removes any whitespace from the beginning or the end
print(len(my_another_string)) #returns the length of a string

#multiline String can be created using three single quotes or double quotes '''hi...ssff''' or """ffjfl...."""
my_multiline_string = '''Lorem ipsum dolor sit amet,
consectetur adipiscing elit,
sed do eiusmod tempor incididunt
ut labore et dolore magna aliqua.'''

print(my_multiline_string)

age = 36
txt = "My name is Greg, and I am "

# print(txt+age) - will produce error, can't concat int and string as such
print(txt+str(age)) #cast int to string and concat
print(txt+"{}".format(age)) #using format we can add the variable we want in a string inside the position{

name = 'Greg'
age = 40

print("My name is {}, and I am {}".format(name,age))
print("My name is {0}, and I am {1}".format(name,age))
print("My name is {1}, and I am {0}".format(age,name))

print(f"My name is {name}, and I am {age}")
