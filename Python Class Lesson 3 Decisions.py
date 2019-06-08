#Lesson 3: Decision Structures

#if statement syntax:
#if <condition>:
#   <statement>
#<statements outside if block>

#Basic example of if statement:
my_dude = "Mike Chen"
if my_dude == "Mike Chen":
    print("My dude is", end=" ")
    print(my_dude)
print("This string is outside the block because of indents, apparently.")
print()

#Python uses Unicode when comparing the value of different characters
letter = "C"
if letter > "B":
    print("The letter is greater than B")
if letter < "D":
    print("The letter is less than D")
print("letter =", end=" ")
print(letter)

#Lowercase letters are less than uppercase letter in Unicode
if letter < "a":
    print("The letter is less than a")
print()

#Syntax for if-else clause:
#if <condition>:
#   <statement>
#else:
#   <false statement>
#<statement outside the if-else clause
poopy_head = True
if poopy_head == True:
    print("You are a poopy head")
else:
    print("You are not a poopy head")
poopy_head = False
if poopy_head == True:
    print("You are a poopy head")
else:
    print("You are not a poopy head")
print()

#else if statements -> elif <statement>:
morningstar = "a"
if morningstar == "b":
    print("morningstar = b")
elif morningstar == "c":
    print("morningstar = c")
elif morningstar == "a":
    print("morningstar = a")
else:
    print("What is morningstar?")

#Logical operators
age = eval(input("How old are you?: "))
registered= input("Are you registered? (y/n): ")
if age >= 18 and registered == "y":
    print("You are ready to vote!")
else:
    print("You are not ready to vote.")
print()

#Syntax for OR operator
upper_or_lower_doesnt_matter = input("Enter Y or y: ")
if upper_or_lower_doesnt_matter == 'y' or 'Y':
    print("You entered Y or y!")
else:
    print("You entered something else")
print()

#Printing a string then a variable
print("The last input:", upper_or_lower_doesnt_matter)
print()

#More on logical operators
length = 20
if length >= 10 and length <= 14: #Tested if this worked: if length >= 10 and <= 14: (did not work)
    print("length is greater than 10 and less than 14")
else:
    print("length is less than 10 or greater than 14")

#FAQ
#Does Python have a "switch" or "case" structure like in other languages? No. (Python sux xd)


