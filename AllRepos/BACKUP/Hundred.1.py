"""
Name:  Kizito Jegede
ID: Codestar007
Course: MSc CS - PoP 1

Assignment Two: (Please refer to 'README.dm' for full details)
Program Title: Hundred
Program Description: An interactive game in which two players takes
                    turns to roll a dice. At the end of each turn, the
                    score for that turn is added to the player's total
                    score. The first player to reach or exceed 100 wins.
"""


def main():
    """This is where your program will start execution."""
	#Initialize variables
    computer_turns = 0
    human_turns = 0
    count_of_turns = 0
    computer_score = 0
    human_score = 0
    game_over = False

    print(instructions(), "\n")
    #pause = input("Hit the RETURN key to continue......") #Pause for player to read instructions
    print("The Game is starting....")

    while not game_over:
        count_of_turns += 1
        human_turns += 1
        computer_turns += 1
        print("\n")
        computer_score += computer_move(computer_score, human_score, computer_turns) # plays first
        print("\n")
        human_score += human_move(computer_score, human_score, human_turns)		 # plays next

		#check if fair play rule needs to be applied
        if computer_score >= 100 and human_score < computer_score:
			#give human one more turn
            human_turns += 1
            human_score += human_move(computer_score, human_score, human_turns)
		#check if players are tied and give each another turn until tie breaks
        else:
            while tie_check(computer_score, human_score):
                count_of_turns += 1
                human_turns += 1
                computer_turns += 1
                computer_score += computer_move(computer_score,  # plays first
                                                human_score, computer_turns)
                print("\n")
                human_score += human_move(computer_score, human_score, human_turns)		 # plays next

		#check if game is over
        game_over = is_game_over(computer_score, human_score)

    if game_over: return show_results(computer_score, human_score)

def instructions():
    """This function tells the player the rules of the game."""
    return """Below are the rules of the game:
    1.  You will take turns to play against the computer
    2.  The computer always plays first
    3.  On each turn, you roll a six-sided die as many times as
        you wish, or until tyou roll a 1
    4.  Each number you roll, except a 1, is added to your
        score this turn
    5.  But if you roll a 1, your score for this turn is zero, and
        your turn ends
    6.  At the end of each turn, your score for that turn is added to
        your total score
    7.  The first player to reach or exceed 100 wins the game.
    8.  if the computer reaches or exceeds 100 first, you will
       get one additional turn
    9.  If you are and the computer are tied with 100 or more,
        you will both get another turn until the tie is broken."""

def human_move(computer_score, human_score, human_turns):
    """This function displays a player's and the computer's current
    score, and how far behind (or ahead) the player is. Then repeatedly
    asks whether the user wants to roll again. This continues until either:

    -   The user decides not to roll again. The function should return the
        total of the rolls made during this move.
    -   The user rolls a 1. The function should return 0.
    """

    roll_count = 0
    player_response = True

    # calls 'current_score' and uses return value to print current score
    print("Turn:", human_turns, "| You\nCurrent scores:",
          "You =", human_score, "| Computer =", computer_score)
    print(current_score(computer_score, human_score))

    # Asks whether the user wants to roll again
    while player_response:
        player_response = ask_yes_or_no("Roll dice again? 'Y'(yes) or 'N'(no):")
        if player_response is False:
            return human_score
        else:
            this_roll = roll()
            roll_count += 1
            if this_roll == 1:
                return 0
            else:
                human_score += this_roll

def current_score(computer_score, human_score):
    """This funcion constructs a comparison between the current human
    and computer_score and returns a string
    """

    score_diff = human_score - computer_score
    if score_diff > 0:
        return "You are " + str(abs(score_diff))  + " points AHEAD of the Computer"
    elif score_diff < 0:
        return "You are " + str(abs(score_diff)) + " points BEHIND the Computer"
    else:
        return "You are level with the Computer at " + str(human_score)
   
def computer_move(computer_score, human_score, computer_turns):
    """This function computes the computer rolls some number of times,
    displays the result of each roll, and the function returns the
    result (either 0 or the total of the rolls). The function may use
    its parameters in order to play more intelligently (for example, it
    may wish to gamble more agressively if it is behind).
    """

    total_of_rolls = 0
    aggressive = 5
    gently = 2

    # Computer selects play style
    if computer_score - human_score <= 0:
        style = aggressive
    else:
        style = gently

    for i in range(1, 1+style):
        this_roll = roll()
        print("Turn:", computer_turns, "| Computer roll:", i,
              "number =", this_roll)
        if this_roll == 1:
            return 0
        else:
            total_of_rolls += this_roll
    return total_of_rolls

def tie_check(computer_score, human_score):
    """Takes as a parameter, the current score of computer and human and then
    checks if there is a tie between them. If there is a tie, the function returns
	a boolean vale True, else it returns False"""
    if computer_score == human_score >= 100: return True
    else: return False

def is_game_over(computer_score, human_score):
    """Returns `True` if either player has 100 or more, and the players are
    not tied, otherwise it returns `False`. (Call this  only after the
    human's move.)"""

    if (computer_score >= 100 or human_score >= 100) and computer_score != human_score:
        return True
    else:
        return False

def roll():
    """Returns a random number in the range 1 to 6"""
    from random import randint
    return randint(1, 6)

def ask_yes_or_no(prompt):
    """Prints the prompt as a question to the user, for
    example, `"Roll again? "`. If the user responds with a string whose
    first character is `'y'` or `'Y'`, the function returns `True`. If
    the user responds with a string whose first character
    is `'n'` or `'N'`, the function returns `False`. Any other response
    will cause the question to be repeated until the user provides an
    acceptable response.
    """

    response = input(prompt)
    try:
        if response[0] == "Y" or response[0] == "y":
            return True
        elif response[0] == 'N' or response[0] == 'n':
            return False
        else:
            return ask_yes_or_no(prompt)
    except IndexError:
        return ask_yes_or_no(prompt)

def show_results(computer_score, human_score):
    """When the game has ended, this function is called to tell
    whether the human player won or lost, and by how much.
    - Arguments (Type):= current computer and human scores (*integer*).
    - Return value type:= *string*.
    """

    if computer_score > human_score:
        return "\nGame Over!! You LOST by: " + str(computer_score - human_score)
    else:
        return "\nGame Over!! You WON by: " + str(human_score - computer_score)

if __name__ == '__main__':
    print(main())
