# Python Problem Sheet 
# Gerard Naughton G00209309
# Part 6
# Objective: Write a function that returns the largest and smallest elements in a list.

# Import Random
import random

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
print(my_list)

# Print out ordered list from highest to lowest. Code adapted from: http://pythoncentral.io/how-to-sort-a-list-tuple-or-object-with-sorted-in-python/
print(sorted(my_list, reverse=True))