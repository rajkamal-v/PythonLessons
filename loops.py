my_string = "hello"

for character in my_string:
    print(character)

known_persons = ["anish", "krishna", "kandan"]

for person in known_persons:
    print("you know {}".format(person))


want_to_continue = True
my_number = 10
while want_to_continue:
    print(my_number)
    my_number += 1
    user_input = input("Do you want to continue (y/n)? ")
    if user_input == 'n':
        want_to_continue = False
