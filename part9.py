# Python Problem Sheet 
# Gerard Naughton G00209309
# Part 7
# Objective: mplement the square root function using Newton’s method. In this case, Newton’s method is to approximate sqrt(x) by picking a starting point z and then repeating:
#z_next = z - ((z*z - x) / (2 * z))
#To begin with, just repeat that calculation 10 times and see how close you get to the answer for various values (1, 2, 3, …). Next, change the loop condition to stop once the value has stopped changing (or only changes by a very small delta). How close are you to the math.sqrt value?

import math
# function loops through the function 10 times to find the answer
def sqRoot1(x, n):
    estimate = x - ((x*x - n) / (2 * x))
    print(estimate)
    for i in range(0,9):
        estimate = estimate - ((estimate*estimate - n) / (2 * estimate))
        print (estimate)

# function loops through the function until the estimate starts to repeat itself
def sqRoot2(x, n):
    oldEstimate = float(x)
    same = False
    estimate = x - ((x*x - n) / (2 * x))
    print (estimate)
    while(same == False):
        if oldEstimate == estimate:
            print(estimate)
            same = True
        else:
            print(estimate)
            oldEstimate = estimate
            estimate = estimate - ((estimate*estimate - n) / (2 * estimate))
    return estimate

#take in values
n = int(input("Enter value you wish to get the square root of? "))
x = int(input("Estimate your answer/starting point? "))

#call function sqRoot1
print("Here is function 1 which loops 10 times")
sqRoot1(x, n)
# call function sqRoot2
print("Here is function 2 which loops until the answer stops changing")
newton = sqRoot2(x, n)
# Check difference for newtons method and math.sqrt
print("Now we will check the difference between newtons method and the math.sqrt value.")
y = math.sqrt(n)
print("The Answer from the math.sqrt is: "+ str(y))
answer = newton - y
print("the difference between Newtons method and math.sqrt is: "+ str(answer))



