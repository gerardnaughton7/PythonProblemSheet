# Python Problem Sheet 
# Gerard Naughton G00209309
# Part 8
# Objective: Write a function that merges two sorted lists into a new sorted list. [1,4,6],[2,3,5] → [1,2,3,4,5,6].

# Import merge from heapq
from heapq import merge

# Simplist version to merge is using the import merge. Adapted from: https://stackoverflow.com/questions/464342/combining-two-sorted-lists-in-python 
def merge_list(l1, l2):
    return list(merge(l1, l2))

# Second version add l2 to l1 and then sort the list
def merge_list2(l1, l2):
    l1.extend(l2)
    m = sorted(l1)
    return m

# create 2 lists
list1 = [1,4,6]
list2 = [2,3,5]

# Output both methods to console
print(merge_list(list1, list2))
print(merge_list2(list1, list2))
