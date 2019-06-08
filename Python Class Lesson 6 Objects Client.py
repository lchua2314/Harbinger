#Lesson 6: Object Client Program
from PythonClassLesson6Objects import Time #Cannot have spaces for "from" file name
print("Creating myTime1 object...")
myTime1 = Time()
myTime1.print_time() #This function here. So a class in Python does not need
myTime1.set_time(1,1,1) #a default constructor in order to work.
myTime1.print_time() #Try to comment out the default constructor and the line 2 above
                    #The program will run just fine.

#Second object can be created
from PythonClassLesson6Objects import Time
print("Creating myTime2 object...")
myTime2 = Time()
myTime2.print_time()
myTime2.set_time(1,2,3)
myTime2.print_time()

#Python Problem - Client program can access data fields without using any class
#function
print("Changing myTime2's hour to 50 through client program")
myTime1.hour = 50
myTime1.print_time()

#To fix this, use double underscore (__) for data fields (variables in class)
from PythonClassLesson6Objects import Time2
print("Creating Time2 object")
myTime3 = Time2()
myTime3.print_time()
myTime3.set_time(3,2,1)
myTime3.print_time()
print("Changing Time2's __hour to 50 through client program")
myTime3.__hour = 50
myTime3.print_time()
print("Testing setter and getter methods") #This is called name mangling

myTime3.set_hour(15) #Which means to indirectly accessing the variables in a class
myTime3.set_minute(14)
myTime3.set_second(13)

myTime3.print_time() #Setter methods work

print("myTime3's hour (INCORRECT):", end=" ")
print(myTime3.__hour) #Prints 50 which is incorrect; This should result in an error.

print("myTime3's hour(2):", end=" ")
print(myTime3._Time2__hour) #Use this. Prints 15 which is correct. USE THIS! IT GOES THROUGH THE GETTER FUNCTION APPARENLTY(?)

#print("Hour:", myTime3.get_hour) #This prints out where the data is stored which is not what I want.

#Changed the getter function for hour
print("myTime3's hour(3):", end=" ")
myTime3.get_hour() #The function will print out the hour

print("Minute:", myTime3.get_minute) #This prints out where the data is stored which is not what I want.
print("Second:", myTime3.get_second) #This prints out where the data is stored which is not what I want.

#Special Attributes

#Documenting - obtains the triple quotation string at the beginning of the class
print(myTime3.__doc__)
print(Time2.__doc__) #This would also work if you do not have an object yet

#Class name
print(myTime3.__class__)


