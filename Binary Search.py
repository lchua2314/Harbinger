print("------------------------------Binary Search------------------------------\n")

the_list = []
sentinel = "go"

while sentinel != "": #Needs a way to end the loop without using a number and you cannot use any deimals here.
    user_input = input("Please enter a number(Press Return to stop):")
    if user_input == "":
        break
    else:
        the_list.append(eval(user_input))
    
    #try:
    #    user_input = int(input("Please enter a number(-999 to stop):"))
    #except ValueError:
    #    print("Invalid input!")
    #if user_input == -999:
    #   break
    #the_list.append(user_input)
    
    
#print(the_list)

#if user_input == -999:
#            sentinel == ""

print(the_list)

print("Sorting list...")
the_list.sort()

print("Sorted List:", the_list)
print("Length of List:", len(the_list))

if len(the_list) % 2 == 0:
    print("Appending -999 to the list because the list has to be odd for binary search to work.")
    the_list.append(-999)
    print("New list:", the_list)

user_input = int(input("Please enter a number to search the list:"))

def recursive_binary_search(number, list_length):
    #index = len(the_list)/2
    index = int(list_length / 2) #012345678
    if the_list [index] == number:
        print("It is in the list")
    elif the_list [index] > number:
        recursive_binary_search(number, index*3)
    elif the_list [index] < number:
        recursive_binary_search(number, index)
    else:
        print("It is not in the list")

recursive_binary_search(user_input, len(the_list))

#sentinel3 = "go"
#while sentinel3 != ""
#index = len(the_list)/2
#if the_list [user_input] == user_input:
    #print("It is in the list")
#elif the_list [user_input] > user_input:
    
#elif the_list [user_input] < user_input:
