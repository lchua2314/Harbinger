#Lesson 5: Functions

#Function syntax
#def <function name> (<parameter list>):
#    <doucementation string>
#    <the function's code>

def welcome_gamer ():
    """Greets the gamer."""
    print("Hello, gamer!")

welcome_gamer()

#Parameter use
def print_value (value):
    """Prints input value"""
    print("This is your value:", value)

input_value = eval(input("Please input a value: "))
print_value(input_value)

#Doesn't matter if it is a string or int or whatever
string_value = "This is a string. You don't say?"
print_value(string_value)

#Changing values from inside a function?
def change_value (value):
    """This function changes the value passed in to 1"""
    print("Inside, value is:", value)
    value = 1
    print("Inside, value is changed to:", value)
number = 5
print("Outside, number is:", number)
change_value(number)
print("Outside, number is now:", number)
#number is not changed to 1 because it is out of scope.

#Global statement
#global <variable_name>
def change_number ():
    """This function changes the value passed in to 1 (global)"""
    global number
    number = 1
number = 5
print("Outside, number is:", number)
change_number()
print("Outside, number is now:", number)

#Return statement
def square(num):
    return num * num
square(3) #You can write this code without assigning anything to it
print("This is the square of 3 is:", square(3))

for i in range(1,11):
    print(square(i))

#Every Python function has a return. Even ones that you do not define.
print(welcome_gamer()) #Runs the function and prints "None"
#None means null in other languages.

#Default arguement in parameter list
def square(num = 1):
    return num * num
print(square()) #This can be called w/ or w/o a parameter
print(square(4))

#Keyword Arguements - Tells the PC which variables
#in the function's parameter list should
#be storing which values and can be out of order
#ex: print(square(num = 5, other_variable = "Hello"))
print(square(num = 5))
