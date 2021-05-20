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

#     --def sayHello(self):
#         print("Hello, World!")

#     --def checkPassing(self, marks):  # Member Function with Parameters
#         self.marks = marks

#         if self.marks >= 33:
#             print(self.name, " has passed the exam")
#         else:
#             print(self.name, " has failed the exam")

# test_object = TestClass("Fawzaan", 19)

# print("{} is {} years old and has {} the examination".format(test_object.name, test_object.age, test_object.test))

# test_object.sayHello()
# test_object.checkPassing(56)
# test_object.checkPassing(22)

# -- class BasicMathClass:
#     def __init__(self,name,symbol):
#         self.name = name
#         self.symbol = symbol
    
#     def square(self):   # Member Functions with a Return Type
#         return self.symbol * self.symbol
    
#     def cube(self):
#         return self.symbol * self.symbol * self.symbol
    
#     def multiply(self, x): # Member Function with a Parameter and Return Type
#         return self.symbol * x

# basic_math_object = BasicMathClass("Seventeen", 17)

# square_value = basic_math_object.square()
# cube_value = basic_math_object.cube()
# multiply_with_x = basic_math_object.multiply(24)

# print(square_value, " ", cube_value, " ", multiply_with_x)


# ----------- Inheritance -----------
# class SoftwareEngineer:
#     def __init__(self,name,age):
#         self.name = name
#         self.age = age
    
#     def salary(self, value):
#         self.money = value
#         print(self.name, " earns ", self.money)

# software_employee = SoftwareEngineer('Ritveak', 26)
# software_employee.salary(40000)


# class Artist:
#     def __init__(self,name,age):
#         self.name = name
#         self.age = age
    
#     def salary(self,value):
#         self.money = value
#         print(self.name, " earns ", self.money)
    
#     def artform(self, job):
#         self.job = job
#         print(self.name, " is a ", self.job)

# general_employee = Artist('Vraj',20)
# general_employee.salary(50000)
# general_employee.artform('Musician')


# class InheritedArtist(SoftwareEngineer):
#     def artform(self, job):
#         self.job = job
#         print(self.name, " is a ", self.job)

# employee = InheritedArtist("Fawzaan", 19)
# employee.salary(1000)
# employee.artform("Software Engineer")
