#Lesson 4: Loops (While and For)

#Syntax:
#while <condition>:
#   <statement>

num = 1
while num <= 5: #prints 1\n-5\n
    print(num)
    num += 1 #Attempted to do "num++" but that did not work
print("End of while loop 1")

#If you create an infinite loop, use Ctrl + C to end the program

#Counter-controlled loop - A loop that stops after it reachs a certain number of iterations
#Condition loop - A loop that can be stopped when a condition is met.
number = 0
answer = 'y'
while answer == 'y': #prints 1\n, asks for user input of 'y' or anything else
    print(number)    #and keeps cycling until user inputs 'y'
    number += 1
    answer = input("Do you want the next number? (y/n): ")
print("End of while loop 2")

#For Loop syntax:
#for <variable> in <sequence>:
#   <statement>

#First while loop translated to a for loop
for num in range(1,6): #prints 1\n-5\n
    print(num)
print("End of for loop 1")
#This for loop makes sure you never enter an infinite loop
#range() function - list data structure that will be taught in later lesson
#It adds 1 to num for every cycle until it reaches 6 then it ends the loop.
#range(<starting number>,<stop loop number>,<increment number>)

for num in range(6): #prints 0\n-5\n
    print(num)
print("End of for loop 2")

for num in range(1, 10, 2):
    print(num)
print("End of for loop 3")

#Ask user for number of values to average
#Then ask the user for the values
#Print out the average

number_of_values = eval(input("How many numbers would you like to input (Other than 0)?: "))
sum = 0.0
value_num = 1
for count in range(number_of_values): #Python is actually using range(number_of_values, 0, -1) for the range() function
    print("Value", value_num, end="")
    value = eval(input(":"))
    sum += value
average = sum / number_of_values
print("Average: ", average)
print()

#Extra info about loops

#while answer == 'y' or 'Y': will always be true because 'Y' in Boolean means True
#To counter this, use: while answer == 'y' or answer == 'Y':

#The break and continue statements are the same in C, C++, and Java.

#Else clause in a for loop
#This allows the user to know if the loop iterated through all the cycles and not exited through a break
#THIS IS NOT IN ANY OTHER LANGUAGE OTHER THAN PYTHON
for count in range(6):
    if count == 4:
        continue
    print(count)
else:
    print("Exited normally")
#Now with a break statement instead of a continue statement
for count in range(6):
    if count == 4:
        break
    print(count)
else:
    print("Exited normally")
#A good example of when you want to use the else clause in a for loop
#When you are trying to find a letter in a phrase. If it is found, end the loop. If it is not found, print that it is not found.
phrase = input("Enter a phrase: ")
letter = input("Enter a letter: ")
length = len(phrase)

for index in range(0, length):
    if phrase [index] == letter:
        print("Letter", letter, "was found at index[", index, "]")
        break
else:
    print ("Letter", letter, "was not found.")

#Example for nested for loops: Multiplication Table
for i in range(0, 11):
   print ("~~~", i, "~~~")
   for j in range(0, 11):
       print (i*j)
       print ( )

#Link to info about while and for loops with examples: http://en.wikibooks.org/wiki/Python_Programming/Loops
