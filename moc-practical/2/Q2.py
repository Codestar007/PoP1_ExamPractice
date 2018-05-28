from random import randrange

total = 0
randNum = randrange(0,100)
print(randNum)
response = -1
prompt = "Guess a number between 0 and 99: "
while response != randNum:
    total += 1
    response = int(input(prompt))
    if response == randNum:
        print("Correct. It took you", total, "guesses.")
    elif response > randNum:
        prompt = "Too high. Guess again: "
    else:
        prompt = "Too low. Guess again: "
# OR

number = randrange(0,100)
guess = int(input("Guess (0..99): "))
count = 1
wrong = guess != number
while wrong:
    if guess < number:
        print("Too low")
    else:
        print("Too high")
    guess = int(input("Guess again: "))
    count = count + 1
    wrong = guess != number
print("Correct. It took you ", count, " guesses.")