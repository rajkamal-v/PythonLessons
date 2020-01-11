my_list = [0, 1, 2, 3, 4]
an_equal_list = [x for x in range(5)] # 0, 1, 2, 3, 4 same as above
print(an_equal_list)

three_table_list = [x*3 for x in range(1,10)]
print(three_table_list)

even_number_under_10 = [x for x in range(10) if x%2 == 0]
print(even_number_under_10)

people_you_know = ["greg", "Jhon", " Alex", "SIMON", "Peter "]
normalized_people = [people.strip().lower() for people in people_you_know]
print(normalized_people)
