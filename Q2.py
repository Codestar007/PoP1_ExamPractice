import random

total = 0
randNum = random.randrange(0,100)
print(randNum)
response = -1
prompt = "Guess a number between 0 and 99: "
while response != randNum:
    total += 1
    response = int(input(prompt))
    if response == randNum:
        print("Correct. It took you", total, "guesses.")
        #break
    elif response > randNum:
        prompt = "Too high. Guess again: "
        #print("Too high. Guess again: ")
    else:
        prompt = "Too low. Guess again: "
        #print("Too low. Guess again: ")

