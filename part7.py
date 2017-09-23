# Python Problem Sheet 
# Gerard Naughton G00209309
# Part 7
# Objective: Write a function that tests whether a string is a palindrome.

#function to check if work is palindrome
def palindrome(w):
    # first i reverse the word
    rWord = reversed(w)

    # And then compare the reveresed word and the origional and see if they are the same
    if(list(w) == list(rWord)):
        return "The word is a Palindrome!"
    else:
        return "The word is not a Palindrome"

# Get user to input a word to test and change it all to lower case
word = input("Please enter a word? ").lower()

# Call palindrome function and print out result
print(palindrome(word))