""" Python Code for Lambda Functions Explanations and Examples """

""" Lambda Functions are one-liner functions that do not have a name and return a result """

# functionName = lambda variable_name: operation on variable_name

addTen = lambda x: x + 10
print(addTen(29))

# square = lambda x: x * x
# print(square(8))

# ----------- Using two different variables -----------
# add = lambda x, y: x + y
# print(add(2, 3))

# ----------- More variables as parameters -----------
# moreNumbersAdd = lambda x, y, z: x + y + z
# print(moreNumbersAdd(1, 2, 3))

# ----------- Lambda with constant return operands -----------
# constantSubtract = lambda x: 1 - 2
# print(constantSubtract(4))
print()


""" map() function - maps a function to a list and its elements """
print(map(lambda x: x + 2, [1, 2, 3]))
print(list(map(lambda x: x + 2, [1, 2, 3])))

# example_list = [1, 2, 3, 4, 5]
# print(list(map(lambda x: x + 10, example_list)))

# ----------- map() on two lists -----------
# list1 = [1,2,3,4,5,6,7,8,9]
# list2 = [9,8,7,6,5,4,3,2,1]
# eg2 = list(map(lambda x, y: x + y, list1, list2))
# print(eg2)

# ----------- map() with built-in functions -----------
# eg3 = map(str, eg2)
# print(list(eg3))
print()


""" filter() unction is used to filter out the values in a list """
list1 = [1, 2, 3, 4, 5, 6, 7, 8, 9]
print(list(filter(lambda x: x < 5, list1)))
# print(list(map(lambda x: x < 5, list1)))

# ----------- Voting Eligibility example using filter -----------
# ages = [20, 19, 56, 10, 23, 14, 15, 20]
# eligible_to_vote = list(filter(lambda x: x >= 18, ages))
# print("The following ages are eligible to vote - {}".format(eligible_to_vote))
print()
