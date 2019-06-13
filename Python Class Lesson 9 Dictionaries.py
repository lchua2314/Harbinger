#Lesson 9: Dictionaries

#Key - The ability to quickly and easily find an item comes from a speicla and unique value calle a key.
#Key-value Pair - Each entry in the dictionary. (AKA hashes or associative arrays)

#Creating a dictionary
my_dictionary = {}

#Required to have the key:value
days_in_month = {'Jan':31}

#It is possible to use mutiple data types for keys, but it can be confusing.
#Many data types can be used for keys and values.

print("Printing out days_in_month['Jan']:", days_in_month['Jan'])

days_in_month = {'Jan':31, 'Feb':28, 'Mar':31}

#Printing out the keys and values could be in a different order from the code.
#This is to reduce the time to run the code.
print("Printing all keys and values in days_in_month:\n", days_in_month)

#keys() and values() functions
#Order will not always be the same as the code.
#The output comes out with a list so it can be saved in a variable with ease.
print("Printing all keys:", days_in_month.keys())
print("Printing all values:", days_in_month.values())

#I don't know how to store it in a list.
meh_keys = days_in_month.keys()
print("Printing 'meh_keys':", meh_keys)

#items() returns key-value tuples.
print("Printing items() function:", days_in_month.items())

#KeyError - A syntax error in which key is not found in a dictionary.
#To avoid this use this:
print("Is 'Feb' key in days_in_month?:", 'Feb' in days_in_month) #Prints True because 'Feb' key is in days_in_month

#Creates a new key-value to my dictionary
days_in_month['Apr'] = 20
#Changes the value
days_in_month['Apr'] = 30

#update() function allows you to add a dictionary to another dictionary.
days_in_month2 = {'May':31, 'Jun':30, 'Jul':31}
days_in_month.update(days_in_month2)
print("Printing days_in_month updated version:\n", days_in_month)

#del keyword deletes a key-value from a dictionary.
#Note: Yow will get KeyError error if the key is not found in the dictionary.
#Also, you can delete the whole dictionary at once.
del days_in_month['Apr']
print("Deleted 'Apr' key with the value:\n", days_in_month)

#clear() function clears all key-values in the dictionary.
days_in_month.clear()
print("Cleared days_in_month:", days_in_month)

#get() function allows you to obtain the value or 'None' if there is no key-value.
print("Using get() function for 'Jan' in days_in_month:", days_in_month.get('Jan'))
print("Using get() function for 'May' in days_in_month2:", days_in_month2.get('May'))
#Can also put a default output if the key is not found.
print("Using get() function for 'Jan' with default value instead of 'None' in days_in_month:\n", days_in_month.get('Jan', "'Jan' is not found."))

#Creating a dictionary that will ask for user input and then print out all values and their value count.
print("Starting dictionary consistency code...")
words = {}
value = input("Please enter a word (or -999 to quit):")
while(value != '-999'):
    if value in words: 
        words[value] = words[value] + 1
    else:
        words[value] = 1

    value = input("Please enter a word (or -999 to quit):")

for current_key in words.keys(): #Random order
    print(current_key, '\t', words[current_key])

print("Ending dictionary consistency code...\n")

#Another way to do the for loops above except with a list.
my_keys = list(words.keys())
my_keys.sort()
for current_key in my_keys:
    print(current_key, '\t', words[current_key])

#Whatever this does...

#Teacher's code that stores info about student test grades in a dictionary.

#Links:
#Word counter program(downloads a file): 
