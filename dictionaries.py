#A dictionary is a collection which is unordered, changeable and indexed.
#In Python dictionaries are written with curly brackets, and they have keys and values.


thisdict =	{
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
print(thisdict)

#dictionary can be created using dict() constructor

dict_cars = dict(brand="hyundai", model="i20", year=2017)
# note that keywords are not string literals
# note the use of equals rather than colon for the assignment
print(dict_cars)

#You can access the items of a dictionary by referring to its key name, inside square brackets:
x = thisdict["model"]
print(x)

# or we can use the get() method to access the items
x = thisdict.get("model")
print(x)

#Change values
thisdict["year"] = 2019
print(thisdict)

#Print all key names in the dictionary as a list using list comprehension
print([x for x in thisdict])

#print all the key names in the dictionary using keys() method
x = thisdict.keys()
print(x)

#Print all value in the dictionary as a list of string, using list comprehension
print([str(thisdict[x]) for x in thisdict])

#Print all key names in the dictionary one by one
for x in thisdict:
    print(x)

#print all values in the dictionary one by one
for x in thisdict:
    print(thisdict[x])

#You can also use the values() function to return values of a dictionary:
for value in thisdict.values():
  print(value)

#Loop through both keys and values, by using the items() function:
for key, value in thisdict.items():
  print(key, value)

#Check if Key Exists -  use the keyword 'in'
if "model" in thisdict:
  print("Yes, 'model' is one of the keys in the thisdict dictionary")

#Dictionary Length
print(len(thisdict))

#Adding Items in a Dictionary
thisdict["color"] = "red"
print(thisdict)

#Removing Items
my_dictionary = {"name":"Jhon", "id":"jc4566", "department":"csc", "age":36, "band":"E1.1"}

my_dictionary.pop("band") #removes band item from the dictionary
print(my_dictionary)

del my_dictionary["department"]
print(my_dictionary)

my_dictionary.popitem()  #removes a random item
print(my_dictionary)

my_dictionary.clear()  #The clear() keyword empties the dictionary
print(my_dictionary)

del my_dictionary  # delete my_dictionary dictionary itself
#print(my_dictionary) #this will cause an error because "my_dictionary" no longer exists.
