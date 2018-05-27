from random import *
myRand = int(random() * 99)
print(myRand)
#myRand = 54
totalGuess = 0
prompt = "Guess a number between 0 and 99: "
response = -1
while myRand != response:
    totalGuess += 1
    response = int(input(prompt))
    if myRand == response:
        print("Correct. It took you", str(totalGuess), "guesses.")
    elif myRand > response:
        prompt = "Too low. Guess again: "
    else:
        prompt = "Too High. Guess again: "

#pritnt(myRand)
