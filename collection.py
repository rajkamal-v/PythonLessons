grades = [70, 80, 90] #List - ordered and mutable
tuple_grades = (70, 80, 90) #Tuple - ordered and immutable
set_grades = {70, 80, 90} #Set - unordered and unique

print(sum(grades)/len(grades))
print(grades)
grades.append(100)
print(grades)
print(grades[0])
grades[0] = 60 # replaces 1st element with 60 in the List
print(grades)

print(sum(tuple_grades))
#adding two tuples and reassigning to the same variable
tuple_grades = tuple_grades + (100,) #one element tuple should have a comma at last, else it will be just a number
print(tuple_grades)
tuple_grades = tuple_grades + (20, 30)
print(tuple_grades)
#we cannot assign any element to a tuple like below
# tuple_grades[0] = 99 # not possible as a tuple is immutable


print(sum(set_grades))
#we cannot assign any element to a set like below
# set_grades[0] = 99 # not possible, as a set is unordered it doesnt know which element to replace

#Add element to a set
set_grades.add(100)
print(set_grades)

#Set Operations
set_one = {1, 2, 3, 5, 7}
set_two = {1, 3, 4, 7, 9, 10}

print(set_one.intersection(set_two)) #commmon
print(set_one.union(set_two)) #all but unique
print(set_one.difference(set_two)) #difference 2, 5
print(set_two.difference(set_one)) #difference 4, 9, 10
