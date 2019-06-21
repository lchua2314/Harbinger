#Lesson 11: Handling Exceptions

#Using Try and Except blocks
try:
    bypass_error = 10 #If you try tpying this variable in, it will bypass the exception.
#This is because Python will look for the variable name and apply it if found but if you put
#a string that is not a variable in the program, it will go to the exception block.
    age = eval(input('Please enter your age: '))
    ten_years = age + 10
    print("In 10 years, you'll be", ten_years)
except NameError: #If entered a string, jump to this block immediately.
    print("You must enter a number for your age")
except SyntaxError:
    print("You must enter a number for your age")

print("Have a nice day. Goodbye.")

#Same function, but simplified
try:
    bypass_error = 10 #If you try tpying this variable in, it will bypass the exception.
#This is because Python will look for the variable name and apply it if found but if you put
#a string that is not a variable in the program, it will go to the exception block.
    age = eval(input('Please enter your age: '))
    ten_years = age + 10
    print("In 10 years, you'll be", ten_years)
except (NameError, SyntaxError): #If entered a string, jump to this block immediately.
    print("You must enter a number for your age")

print("Have a nice day. Goodbye.")

#Been using the word hierarchy instead of list. Every exception is an object.

#Similar funcation, all exceptions
try:
    bypass_error = 10 #If you try tpying this variable in, it will bypass the exception.
#This is because Python will look for the variable name and apply it if found but if you put
#a string that is not a variable in the program, it will go to the exception block.
    age = eval(input('Please enter your age: '))
    ten_years = age + 10
    print("In 10 years, you'll be", ten_years)
except Exception: #All exceptions are inherited by Exception object
    print("You must enter a number for your age")

print("Have a nice day. Goodbye.")

#Similar funcation, NameError exception before Exception object
try:
    bypass_error = 10 #If you try tpying this variable in, it will bypass the exception.
#This is because Python will look for the variable name and apply it if found but if you put
#a string that is not a variable in the program, it will go to the exception block.
    age = eval(input('Please enter your age: '))
    ten_years = age + 10
    print("In 10 years, you'll be", ten_years)
except NameError: #If you switch this exception block with the one below, NameError will never be caught because Exception already caught it. 
    print("NameError occured")
except Exception: #All exceptions are inherited by Exception object
    print("You must enter a number for your age")

print("Have a nice day. Goodbye.")

#List Index Out of Range (bounds in other languages) Error
try:
    my_list = [0,1,2]
    print(my_list [4])
except IndexError as ie:
    print(ie)

#IOError
try:
    infile = open('myfile.txt', 'r')
    infile.write("hello")

    infile.close()
except IOError as ioe:
    print(ioe.filename)
    print(ioe.strerror)

#dir() method - complete list of all of the attributes of this IOError object
print(dir(IOError))

#Else block - Only runs if no exception occurs
try:
    user_num = eval(input("Please enter a number: "))
    result = 10 / user_num
except (NameError, SyntaxError):
    print("The value you entered was not a number")
except ZeroDivisionError:
    print("You Cannot divide by zero")
else:
    print("The result of dividing by your number is", result)

#Finally block - Will run no matter what
try:
    infile = open('data.txt', 'r') #First, dont create a file named data.txt, then create one and put a number, letter, etc. Keep testing it out.
    try:
        value = infile.readline()
        number = int(value)
        print(number)
    finally:
        infile.close()
        print("the data file was closed")
except IOError as io:
    print("Could not open file:", io.filename)
except ValueError:
    print("Could not convert", value, "to a number")
