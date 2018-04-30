import random

total = 0
randNum = random.randrange(0,100)
response = -1
prompt = "Guess a number between 0 and 99: "
while response != randNum:
    total += 1
    response = int(input(prompt))
    if response != randNum:
        print("Correct. It took you", total, "guesses.")
        break