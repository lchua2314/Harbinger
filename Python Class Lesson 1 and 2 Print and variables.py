#Lesson 1: print() function
print("Hello, Computer!")
print('I AM VERY SMART\n')
print("HELLOHELOGWLO\n")

#Lesson 2: Variables & keyword.kwlist

#Variables are usually named with underscores instead of uppercase letters.
#For example: jeffersonStarship
#This is how variables are declared in C, C++, and Java.
#For Python, people do: jefferson_starship

#Why have quote usage
quote = 'The women said "Hello"'
print(quote) 

quote = "The women said \"Hello\"\n"
print(quote)

#Printing keywords
print("Keywords: ")
import keyword
print(keyword.kwlist)
print()

#Variables can be changed to whatever primitive daya type
name = 'Python'
name = "Python"
name = 123
print(name)
print()

#Variables can be assigned in the same line in this way
a, b = 1, 2
print(a)
print(b)
print()

#input function:
#When using a string, 
#<variable> = input(<Prompt>)
hi_my_name_is = input("Name: ")
print(hi_my_name_is)

#When using a number, you must convert from string to int?
#<variable> = eval(input(<Prompt>))
age = eval(input("Age: "))
age += 10
print("Your age 10 years from now: ")
print(age)
print()

#How to exponent numbers?
a = eval(input("Powering your next two values: "))
b = eval(input("Power: "))
print(a ** b)
print()

#import statement
#Importing math library
import math
print("THe value of Pi is:")
print(math.pi)
print("Using the power function: print(math.pow(2,3))")
print(math.pow(2,3))
print()

#More with strings
print("This line the two time! " * 2)
print()

length = "My words are whirlwinds."
print(length)
print("The length of this string is: ")
print(len(length))
print()

#Indexing and slicing strings
print("Indexing and slicing strings: ")
phrase = "Python though"
print(phrase [0])
print(phrase [1:3])
print(phrase [7:14])
print(phrase [7:])

print("Changing phrase to lowercase 'p' instead of 'P'")
phrase = 'p' + phrase [1:] #Placing lowercase 'p' instead of 'P'
print(phrase)

#FAQ

#Trying to print last name with a string called "Pat White" but last letter won't print
pat_name = "Pat White"
print(pat_name)
print(pat_name[4:8]) #Will print "Whit" because Python will not print the last index (8 in this case)
print(pat_name[4:]) #Just use this instead
print(pat_name[4:9]) #But wait, this works too... I guess it is easier with the one above

#How to tell a print() function without the auto-new line feature
value1 = 1
value2 = 2
print(value1, end = " ")
print(value2, end = " ")
print(pat_name)
