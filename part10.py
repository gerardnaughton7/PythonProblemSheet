# Python Problem Sheet 
# Gerard Naughton G00209309
# Part 10
# Objective: Write a function to reverse a string

# function to reverse a string. I have used this slice sentax before in part 7 of the problem sheet. Adapted from same:  https://stackoverflow.com/questions/17331290/how-to-check-for-palindrome-using-python-logic
def str_reverse(str1):
    return str1[::-1]

str1 = input("Please enter a word? ").lower()

print(str_reverse(str1))