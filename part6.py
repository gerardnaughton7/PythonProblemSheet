# Python Problem Sheet 
# Gerard Naughton G00209309
# Part 6
# Objective: Write a function that returns the largest and smallest elements in a list.

# Import Random
import random

# function to find largest and smallest
def sortList(l):
    min_value = None
    max_value = None
    # Loop around list
    for value in l:
        if not min_value:
            min_value = value
        elif value < min_value:
            min_value = value
        if not max_value:
            max_value = value
        elif value > max_value:
            max_value = value
    # Return the max and min number
    return  "Max number is "+ str(max_value) + " and Min number is "+ str(min_value) +"."

# Alternatively you can do this 
def sortList2(l):
    large = max(l)
    small = min(l)

    return "Max number is "+ str(large) + " and Min number is "+ str(small) +"."

# Declare a list and variables
my_list = []
num = 0
n = 0

# using while loop to generate random list of integers between 1 and 20
while (n != 5):
    num = random.randint(1,20)
    # If not in my_list already apend it to the list
    if(num not in my_list):
        my_list.append(num)
        n = n + 1

# Print out unordered list
print("This is my unordered list" +str(my_list))

# Print out Largest and smallest in the list. Code adapted from: https://stackoverflow.com/questions/27009247/python-find-min-max-and-average-of-a-list-array
print("Using first function the " + sortList(my_list))
# Second function sortList2
print("Using second function the " + sortList2(my_list))