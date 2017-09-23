# Python Problem Sheet 
# Gerard Naughton G00209309
# Part 4
# Objective: Write a function that calculates the sum of the digits of the factorial of a number. n! means n x (n − 1) … x 3 x 2 x 1. For example, 10! = 10 x 9 x … x 3 x 2 x 1 = 3628800, and the sum of the digits in the number 10! is 3 + 6 + 2 + 8 + 8 + 0 + 0 = 27. Find the sum of the digits in the number 100!

# Code for suming of digits adapted from : https://stackoverflow.com/questions/14939953/sum-the-digits-of-a-number-python

# Created a function Factorial to calculate the factorial of n
def factorial(n):
    x = n
    for i in range(1, n):
        x = x*(n-i)
    return x

# Sums up each digit in the string 
sumOfDigits = sum(int(digit) for digit in str(factorial(100)))
# Outputs answer to the console
print("The sum of digits for factorial 100 is " +str(sumOfDigits))