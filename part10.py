# Python Problem Sheet 
# Gerard Naughton G00209309
# Part 10
# Objective: Write a function to reverse a string

# function to reverse a string. I have used this slice sentax before in part 7 of the problem sheet. 
# Adapted from same:  https://stackoverflow.com/questions/17331290/how-to-check-for-palindrome-using-python-logic
def str_reverse(str1):
    return str1[::-1]

# function 2 puts the string into a list. then using the pop function on the before List we remove and return the last element of the list and append it to the after List.
# we loop through the list until all elements have been appended. Adapted from : https://www.tutorialspoint.com/python/list_pop.htm
def str_reverse2(str2):
    before = list(str2)
    after = list()
    while len(before) > 0:
        after.append(before.pop())

    return ''.join(after)

# Input string 1
str1 = input("Please enter a word? ").lower()
# print out result using str_reverse function
print(str_reverse(str1))

# input string 2
str2 = input("Please enter a word? ").lower()
# print out result using ste_reverse2
print(str_reverse2(str2))