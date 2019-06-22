from math import floor  #cause we need da floor function only

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
    the_list.sort()
    print("New list:", the_list)



user_input = int(input("Please enter a number to search the list:"))

while user_input != '':

    copy_list = the_list[:] #returns copy of list. we dont want to permanently change the original list
    print(copy_list)



    #left_bound = copy_list[0]
    #right_bound = copy_list[-1]
    start_point = floor(len(copy_list) / 2)

    #if user_input == copy_list[start_point]:
     #   best_case = True
    #else:
       # best_case = False'''

    while len(copy_list) > 1:  #in worst case, the program will run until there is only one element left in the list.
       # if best_case == True:
            #break
        if user_input == copy_list[start_point]: #checks if the start_point what we
        #    best_case = True
            break
        if user_input > copy_list[start_point]:
            if len(copy_list[start_point:]) % 2 == 0:          #when i cut the list in "half", there are two scenarios. the halved list will either contain the startpoint or not.
                copy_list = copy_list[start_point+1:]          #the halved list must always be odd length. If it is even then start_point will not be the mEDIAN of the list anymore
                start_point = floor(len(copy_list) / 2)   #and the program will not work.
            else:
                copy_list = copy_list[start_point:]
                start_point = floor(len(copy_list) / 2)
            print(copy_list) #I print the new list every iteration to help you visualize how the code works
            continue   #we don't want the other blocks of code to run during the current iteration
        if user_input < copy_list[start_point]:
            if len(copy_list[:start_point+1]) % 2 == 0: #EVEN LIST SCENARIO
                copy_list = copy_list[:start_point]   #slices the list from first element up to but not including the midpoint
                start_point = floor(len(copy_list) / 2)
            else:                                       #ODD LIST SCENARIO
                copy_list = copy_list[:start_point+1] #slices the list from first element up to and including midpoint
                start_point = floor(len(copy_list) / 2)
            print(copy_list)
            continue

    if (copy_list[0] == user_input) or (user_input == copy_list[start_point]):
        print("It is in the list")
    else:
        print("It is not in the list")
    try:
        user_input = int(input("Please enter a number to search the list(return to quit):"))
    except ValueError:
        break

    
    
    











#def recursive_binary_search(number, list_length):
    #index = len(the_list)/2
#    index = round(iWnt(list_length / 2)) #012345678
#    if the_list[index] == number:
 ##       print("It is in the list")
#    elif the_list[index] > number:
 ##       recursive_binary_search(number, index*3)
    #elif the_list[index] < number:
  #      recursive_binary_search(number, index)
  #  else:
    #    print("It is not in the list")

#recursive_binary_search(user_input, len(the_list))

#sentinel3 = "go"
#while sentinel3 != ""
#index = len(the_list)/2
#if the_list [user_input] == user_input:
    #print("It is in the list")
#elif the_list [user_input] > user_input:
    
#elif the_list [user_input] < user_input:

