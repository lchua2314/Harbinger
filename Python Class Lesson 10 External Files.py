#Lesson 10: External Data Files

#open() function parameters: (file name, w to open)
#Opens a data file then stores the file object in the variable
#File should be created where ever the source code file is.
out_file = open('mydata.txt', 'w')
#If you want to create the file in a different location, state the path in the first parameter.
#If you already have a file named the above, it will be overwritten.

#write() function allows you to write a single string into the file.
out_file.write('Hello')
out_file.write(' World\n') #Both of these lines would write out 'Hello World' in the file.

weekends = ['Saturday', 'Sunday']
out_file.writelines(weekends)
out_file.writelines(weekends) #Output would be "SaturdaySundaySaturdaySunday" in the file.

#The file might not be updated immediately because the file access is a time consuming operation.
#flush() function allows the data to be written in immediately.
out_file.flush()

#close() allows you to close the file.
out_file.close()

#Reading data into a file with 'r' parameter in the open() function
in_file = open('mydata.txt', 'r') #The variable name is changed based on convience to the programmer to know what he or she is doing with the file.

#read(), readline(), and readlines() functions
first = in_file.read(1) #Takes the 'H' in Hello. The '1' in the parameter means 1 byte.
second = in_file.read() #Takes the rest of the lines except 'H'
print(first, second)

#readline() works the same way
#readlines() saves the strings from the file and put them in a list.
#print(in_file.readlines()) #This line will leaves a new line empty because the program already read in the rest of the data in the file.

#close() closes the file
in_file.close()

#To keep the file from resetting the data, use the 'a' parameter which stands for append
out_file = open('mydata.txt', 'a')

#Other parameters could be 'r+' and 'w+'. Both options allow you to read and write in the file.
#However, if you do 'r+' and do not have the file created already, there will be an IOError exception.
#If you did 'w+' while already have a file with the same name, the program will delete the file and create a new one.

#tell() function allows you to find out where you are reading from which byte.
#in_file = open('mydata.txt', 'r+')
#print(in_file.read(1))
#print(in_file.tell()) #Output is '1' because you have read 1 byte already.
#Note: '\n' counts as 2 bytes.

#seek() function allows you to move to a new location.
#in_file.seek(0) #Location is before the first byte.
#Warning: If you seek() and then start writing in the file, you will overwrite any data that is already there.

#Pickling - A process that converts an object to a stream of bytes which can be reconverted back to an object later.
#dumps() if you want to store the result in a string.
#dump() stores the result in a file.
import pickle
letters = ['a', 'b', 'c']
pickled_letters = pickle.dumps(letters) #Stores the list as bytes that is placed into a variable
print(pickled_letters) #Prints out the location of the bytes? In RAM?

#Now for storing in a file.
outfile = open('data.txt', 'wb') #'wb' write bytes
letters_file = ['a', 'b', 'c']
pickled_letters_file = pickle.dump(letters_file, outfile)
outfile.close()

#Get the string back from byte form from a variable?
#loads() 
unpickled_letters = pickle.loads(pickled_letters)
print(unpickled_letters) #Prints the list of pickled_letters

#Get the string back from byte form from a file?
#load()
infile = open('data.txt', 'rb') #'rb' read bytes
file_data = pickle.load(infile)
infile.close()
print(file_data)

#Pickling is handy because you can converty your data into bytes and cram them into an external file (which can be retrieved)

#Shelf - A database-like object taht ca efficiently store pickled values. In reality, it is an external data file that is used the same way as a Python dictionary.
#AKA can store a ton of data.
#Parameters: 'c' - opens a shelf for reading and writing, 'n' - create a new, empty file no matter what
import shelve
db_file = shelve.open('letters.txt', 'c')
db_file ['vowels'] = ['a', 'e', 'i', 'o', 'u']
db_file ['end'] = ['x', 'y', 'z']
db_file.close()
#list(), del, and 'vowels' in db_file are the same dictionary uses as an ordinary dictionary.

#sync() allows you to write the files immediately
db_file.sync()

#Links:
#1. Link to teacher's code: https://lo-ed2go-files.difference-engine.com/Resources/py3-0/PY3_L10_Solution_a.py
#2. Info on Pickling: http://docs.python.org/py3k/library/pickle.html
