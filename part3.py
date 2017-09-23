# Python Problem Sheet 
# Gerard Naughton G00209309
# Part 3
# Objective: Write a program that prints the numbers from 1 to 100, except for the following conditions. For multiples of three print “Fizz” instead of the number, and for the multiples of five print “Buzz”. For numbers which are multiples of both three and five print “FizzBuzz”.

# Function which prints fizz or buzz or fizzbuzz when number is a multiple of 3, 5 or both.
def fizzbuzz(n):
    #if divisble of 3 and 5 return fizzbuzz
    if n % 3 == 0 and n % 5 == 0:
        return 'FizzBuzz'
    #if divisble of 3 return fizz
    elif n % 3 == 0:
        return 'Fizz'
    #if divisble of 5 return fizz
    elif n % 5 == 0:
        return 'Buzz'
    #if  not divisble of 3 or 5 return n
    else:
        return str(n)

for n in range(1, 101):
    print(fizzbuzz(n)+ "\n")