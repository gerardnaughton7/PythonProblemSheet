# Python Problem Sheet 
# Gerard Naughton G00209309
# Part 6
# Objective: Write a function that returns the largest and smallest elements in a list.

# Import Random
import random

# function to sort list largest to smallest
def sortList(l):
    for index in range(1,len(l)):
        value = l[index]
        i = index-1
        while i>=0:
            # if l[i] is less than value. then make l[i+1] = l[i]. eventually pushing the lower numbers to the end of the list
            if value > l[i]:
                l[i+1] = l[i]
                l[i] = value
                i -= 1
            else:
                break    
    return l

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

# Print out ordered list from highest to lowest. Code adapted from: https://stackoverflow.com/questions/11964450/python-order-a-list-of-numbers-without-built-in-sort-min-max-function
print("This is my ordered list largest to smallest " +str(sortList(my_list)))