#Lesson 8: Lists and Tuples

#List - An array in other languages while a few differences.
print("------------------------Lists---------------------------")
days_of_week = ['Sun', 'Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat']
print("days_of_week [2]:", end=" ")
print(days_of_week [2]) #Prints 'Tue'

print("Printing out the whole list of \"days_of_week\"")
for count in range(7): #Prints out the whole list in order.
    print(days_of_week [count])

print("Another way to print out the whole list:")
for count in range(len(days_of_week)): #Another way to print out the whole list.
    print(days_of_week [count])
days_of_week [0] = 'Sunday' #Changing the element of index 0 from 'Sun' to 'Sunday'

print("Printing all variables in \"days_of_week list\":", end=" ")
print(days_of_week)

#Slicing a list
print("Slicing a list from index 2-4:", end=" ")
print(days_of_week [2:5]) #In Python, the index starts at 2 and ends at 4 instead of 5.

#Python allows the user to use any data type for all elements in a list.
child1 = ['Pat', 5, 6.5]
#The elements in a list can even be another variable, therefore another list!
family = [child1] #Note: You can put lists in a list. family = [['Pat', 5, 6.5]] is equvalent.
print("Printing \"family [0] [1]\":", end=" ")
print(family [0] [1]) #Checks the first index of family, then the second index of child1 which is 5.

#Adding and Removing elements in a List

my_list = [] #Initially empty list

#The append() method adds one element to the back of a list.
my_list.append(10)
print("my_list:", end=" ")
print(my_list)

my_list.append('ten')
print("my_list:", end=" ")
print(my_list)

#The extend() method allows the programmer to append multiple elements in one line.
my_list.extend([20, 'twenty'])
print("my_list:", end=" ")
print(my_list)

#If you forget these functions, you can just concatenate them.
my_list += [30, 'thirty']
print("my_list:", end=" ")
print(my_list)

#The insert() function allows the programmer to squeeze an item into a list by giving the index and item.
#The rest of the the elements move up one (or to the right)
my_list.insert(3, 'Hello, there!')
print("my_list:", end=" ")
print(my_list)

#The remove() method removes the first item in a list that matches the input.
my_list.remove('Hello, there!') #If there was another 'Hello, there!' farther down the list, this function will remove only the first one.
print("my_list:", end=" ")
print(my_list)

#The max() and min() functions find the max and min values in a list
my_numbers = [16, 8, 15, 42, 23, 4]
print("my_numbers:", my_numbers)
print("Finding max value in 'my_numbers':", max(my_numbers))
print("Finding min value in 'my_numbers':", min(my_numbers))
#These functions will work with a list with all string, but will not work in a list with numeric values AND strings.
my_letters = ['a', 'b', 'c', 'd']
print("Finding max value in 'my_letters':", max(my_letters)) #Prints out 'd' because it is a number in Unicode in which each letter is in increasing order.
print("Finding max value in 'my_letters':", min(my_letters))

#The sort() function sorts all values in increasing order
#Cannot work for a list with mixed strings and numeric values
my_numbers.sort()
print("Sorted 'my_numbers':", my_numbers)
#There are arguements that can be used in the sort() function to sort the way you want. Check at the very bottom for a link on how to do this.

#The reverse() function reverses the order of elements in a list.
#CAN work for a list with mixed strings and numeric values
my_numbers.reverse()
print("Reversed 'my_numbers':", my_numbers)
print("Reversed 'my_list':", my_list)

print("\n")

#Tuples - Very similar to lists and use the many of the same functions as lists.
print("------------------------Tuples---------------------------")

days_of_week2 = ('Sun', 'Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat') #Syntax of a tuple
print("Tuple: 'days_of_week2':", days_of_week2)

#You CANNOT change any items in a tuple once they are established or else you will get an error. A word for this is immutable.
#Because a tuple is immutable, it is stored more efficiently in memory. Therefore, your program will run faster with a tuple than a list.
#There are many Python modules that require you to pass a tuple as an arguement or receive a typle back from a function call.

#A good example would be from the Tkinter module used in the last lesson.
#self.myCanvas.create_text(1, 1, text="Hello World", width=70, fill="blue", anchor="nw", justify="center", font=("Times", 16))
#Notice font=("Times", 16) at the end? That is a tuple. So you can write a tuple data type for your font and call the variable back anytime you need it.
#my_font = ("Times", 16)
#self.myCanvas.create_text(1, 1, text="Hello World", width=70, fill="blue", anchor="nw", justify="center", font=my_font)
#self.myCanvas.create_text(100, 100, text="Hello Planet", width=70, fill="blue", anchor="nw", justify="center", font=my_font)

#Tuples are also the return type for many of the Canvas's functions.

from tkinter import *

class MyFrame(Frame):
    def __init__(self):
        Frame.__init__(self)

        self.myCanvas = Canvas(width=150, height=150, bg="white")
        self.myCanvas.grid()

        self.myCanvas.create_rectangle(10, 10, 20, 20, fill="red")
        self.myCanvas.create_rectangle(10, 30, 20, 40, fill="yellow")
        self.myCanvas.create_rectangle(10, 50, 20, 60, fill="blue")

        #The find_enclosed() function finds any shape in the given coordinates (first top left's x and y, then lower right's x and y)
        print("Finds all my shapes") 
        print(self.myCanvas.find_enclosed(0, 0, 30, 70)) #Returns (1, 2, 3) which are the IDs for each rectangle.

        print("Finds middle shape")
        print(self.myCanvas.find_enclosed(0, 25, 30, 45)) #Returns (1,) which means that there is only one shape-the middle one.

        print("Finds no shapes")
        print(self.myCanvas.find_enclosed(0, 0, 1, 1)) #Returns () which means there is no shape found in that region.
        #Each of the returns are tuples. This is important because you can store these tuples in memory and use them to move the shape around.
        #You can use a single loop through the tuple to move each of the shapes around.
         
frame02 = MyFrame()
frame02.mainloop()

#The assignment was to create a program that find the average of a series of numbers provided by the user.
#Store the values in a tuple, repeat the numbers back to the user then print out the average.
#There is no input validation so putting in a string will result in an error.
#If you can improve the code in any way, please do so below the links.
meh = []
x = 0
counter = 0
sum = 0

while x != -999:
    x = eval(input("Please enter a number (-999 quits):"))
    if x != -999:
        meh.append(x)
        counter += 1
        
print("Using the numbers:")
for count in range(counter):
    print(meh [count], end=" ")
    sum += meh [count]
    
print("\nThe average is:", sum / counter)
    
