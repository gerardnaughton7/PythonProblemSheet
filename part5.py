# Python Problem Sheet 
# Gerard Naughton G00209309
# Part 5
# Objective: Write a guessing game where the user must guess a secret number. After every guess the program tells the user whether their number was too large or too small. At the end the number of tries needed should be printed. It counts only as one try if they input the same number multiple times consecutively.

# Import random to generate random number between 1 and 100
import random

# Function to check answer and print if number is to large, to small or correct and the amount of tries it took
def checker(guess):
    if guess == answer:
        return "You Are Correct. You win! It took you "+ str(len(my_tries))+ " tries."
    elif guess > answer:
        return "Your number was too Large"
    elif guess < answer:
        return "Your number was to Small"

# Get a random number to get your answer
answer = random.randint(1,100)
# Declare variables needed
guess = 0
my_tries = []

# Welcome message to the game
print("Welcome to our guessing game." + str(answer))

#create a while loop to keep playing the game until guess is correct
while (guess != answer):
    # Get the user to input a guess
    guess = int(input("Please enter a number between 1 and 100? "))

    # If guess is outside 1 to 100 try again
    if guess < 1 or guess > 100:
        print("Number is not between 1 and 100. Please try again")
    # If guess has already been tried tell the user
    elif guess in my_tries:
        print("you have already tried this number")
    # else add guess to the array my_tries and check if number using checker function
    else: 
        my_tries.append(guess)   
        print(checker(guess))