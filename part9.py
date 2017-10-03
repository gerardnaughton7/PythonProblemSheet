# Python Problem Sheet 
# Gerard Naughton G00209309
# Part 7
# Objective: mplement the square root function using Newton’s method. In this case, Newton’s method is to approximate sqrt(x) by picking a starting point z and then repeating:
#z_next = z - ((z*z - x) / (2 * z))
#To begin with, just repeat that calculation 10 times and see how close you get to the answer for various values (1, 2, 3, …). Next, change the loop condition to stop once the value has stopped changing (or only changes by a very small delta). How close are you to the math.sqrt value?

import math
# Adapted from : https://stackoverflow.com/questions/12850100/finding-the-square-root-using-newtons-method-errors
# function
def sqRoot1(x, n):
    estimate = (0.5*(x+(n/x)))
    print (estimate)
    for i in range(0,10):
        estimate = (0.5*(estimate+(n/estimate)))
        print (estimate)

# function
def sqRoot2(x, n):
    newEstimate = float(x)
    same = False
    estimate = (0.5*(x+(n/x)))
    print (estimate)
    while(same == False):
        if newEstimate == estimate:
            print(estimate)
            same = True
        else:
            print(estimate)
            newEstimate = estimate
            estimate = (0.5*(estimate+(n/estimate)))
    return estimate

#take in value
n = int(input("Enter value you wish to get the square root of? "))
x = int(input("Estimate your answer/starting point? "))

#call function
print("Here is function 1 which loops 10 times")
sqRoot1(x, n)
print("Here is function 2 which loops until the answer stops changing")
newton = sqRoot2(x, n)
print("Now we will check the difference between newtons method and the math.sqrt value.")
y = math.sqrt(n)
print("The Answer from the math.sqrt is: "+ str(y))
answer = newton - y
print("the difference between Newtons method and math.sqrt is: "+ str(answer))



