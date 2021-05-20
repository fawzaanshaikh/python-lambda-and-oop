""" Python Code for Classes Explanations and Examples """

# class ClassName:
#   data_members, memberFunctions

class FirstClass:
    pass

first_class_obj = FirstClass()  # Instance / Class Object of FirstClass created
print(type(first_class_obj))    # The file from which the top-level code is being run is known to have it's variable __name__ set to __main__

# ----------- Working with Constructors -----------
class SecondClass:
    def __init__(self): # Non-Parameterized Constructor
        print("I am in the constuctor")

second_object = SecondClass()

class ThirdClass:
    def __init__(self, name, age):  # Parameterized Constructor
        self.name = name
        self.age = age

third_object = ThirdClass("Fawzaan", 19)
print(third_object.name, third_object.age)

# -----------  -----------


