#!python3

'''
Create a number guessing game
There is a limit of 10 guesses
The program will ask the user to enter an integer from 1 to 100
The program will then tell the user if the number is too high, too low or correct.
If the number is correct, the program will end
If the 10 guesses are used up, the program will say that the user has lost
'''
Instructions= "Number guessing game! This is how you play: \nYou have ten guesses to figure out the number. \nWhen you put a number in, it will say if the number is too high or too low. \nAt the end it will tell you what the number is Lets play! "
print(Instructions)
num=23
for i in range(1, 11):
    numguess= int(input(f"put in your {i} guess"))
    if  numguess==num:
            print("YOU GOT IT!")
            break 
    elif numguess>num:
            print("Guess is too high")
    elif numguess<num:
            print("Guess is too low")



