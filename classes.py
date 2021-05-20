""" Python Code for Classes Explanations and Examples """

# class ClassName:
#   data_members, memberFunctions

class FirstClass:
    pass

first_object = FirstClass()  # Instance / Class Object of FirstClass created
print(type(first_object))    # The file from which the top-level code is being run is known to have it's variable __name__ set to __main__

# ----------- Working with Constructors -----------
# class SecondClass:
#     def __init__(self): # Non-Parameterized Constructor
#         print("I am in the constuctor")

# second_object = SecondClass()

# class ThirdClass:
#     def __init__(self, name, age):  # Parameterized Constructor
#         self.name = name
#         self.age = age

# third_object = ThirdClass("Fawzaan", 19)
# print(third_object.name, third_object.age)

# print(dir(SecondClass))   # dir() function comes very handy in looking into what the class contains and what all method it offers
# print(dir(ThirdClass))
# print(dir(ThirdClass))
# print(dir(third_object))

# ----------- Data Members and Member Functions -----------
# class TestClass:
#     test = "passed" # Data Member

#     def __init__(self, name, age):
#         self.name = name
#         self.age = age

#     def checkPassing(self, marks):  # Member Function
#         self.marks = marks

#         if self.marks >= 33:
#             print(self.name, " has passed the exam")
#         else:
#             print(self.name, " has failed the exam")

# test_object = TestClass("Fawzaan", 19)

# print("{} is {} years old and has {} the examination".format(test_object.name, test_object.age, test_object.test))

# test_object.checkPassing(56)
# test_object.checkPassing(22)

