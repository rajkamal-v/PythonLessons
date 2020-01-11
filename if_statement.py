a = 200
b = 33
if b > a:
  print("b is greater than a")
elif a == b:
  print("a and b are equal")
else:
  print("a is greater than b")


#shorthands
#if statement
if a > b: print("a is greater than b")
#if else statement
print("A") if a > b else print("B")
#if.. elif... else
print("A") if a > b else print("=") if a == b else print("B")


def who_do_you_know():
    want_to_continue = True
    people_you_know = []
    while want_to_continue:
        user_input = input("Enter the person name: ")
        people_you_know.append(user_input)
        do_u_want_to_continue = input("Do u want to continue (y/n)? ")
        if do_u_want_to_continue == 'n':
            want_to_continue = False

    return people_you_know

def who_do_you_know_2():
    user_input = input("Enter the list of known people, seperated by commas: ") #"John, Alex, Robin, Butler"
    known_people = [people.strip() for people in user_input.split(",")]
    return known_people

def ask_user():
    known_persons = who_do_you_know_2()
    name = input("Enter a name: ")
    if name in known_persons:
        print("you know {}".format(name))
    else:
        print("you don't know {}".format(name))

ask_user()
