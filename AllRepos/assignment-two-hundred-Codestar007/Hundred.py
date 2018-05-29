"""
Name:  Kizito Jegede
ID: Codestar007
Course: MSc CS - PoP 1

Assignment Two: (Please refer to 'README.dm' for full specification)
Program Title: Hundred
Program Description: An interactive game in which two players take
                    turns to roll a die. At the end of each turn, the
                    score for that turn is added to the player's total
                    score. The first player to reach or exceed 100 wins.
"""


def main():
    """The program starts execution here. It calls various
    functions to print game instructions, execute computer and human
    player turns, check and apply fair play rule (if required), apply
    tie break and prints the game result.
    """

    computer_turns = 0
    human_turns = 0
    count_of_turns = 0
    computer_score = 0
    human_score = 0

    instructions()  # print game instructions
    while not is_game_over(computer_score, human_score):
        play_result = play_game(count_of_turns, computer_turns,
                                computer_score, human_turns, human_score)
        (count_of_turns, computer_turns, computer_score, human_turns,
         human_score) = play_result

		# Apply fair play rule if required; human gets one more turn
        if computer_score >= 100 and human_score < computer_score:
            human_turns += 1
            print("\nTurn:", human_turns, " (Fair play) | You")
            human_score += human_move(computer_score, human_score)

        while computer_score == human_score >= 100:  # Tie breaker.
            play_result = play_game(count_of_turns, computer_turns,
                                    computer_score, human_turns, human_score)
            (count_of_turns, computer_turns, computer_score, human_turns,
             human_score) = play_result

    show_results(computer_score, human_score)  # Print result

def play_game(count_of_turns, c_turns, c_score, h_turns, h_score):
    """Function is implemented to streamline the lenght of code in
    "main()". It takes 5 parameters; count of turns, computer
    turns, computer score, human turns, human score and returns the
    updated values as a 5 tuple (int).
    """

    # Computer Move call
    count_of_turns += 1
    c_turns += 1
    print("\nTurn:", c_turns, "| Computer")  # Computer's header
    c_score += computer_move(c_score, h_score)

    # Human Move call
    h_turns += 1
    print("\nTurn:", h_turns, "| You")  #  Human's header
    h_score += human_move(c_score, h_score)

    return (count_of_turns, c_turns, c_score, h_turns, h_score)

def instructions():
    """This function tells the player the rules of the game."""
    print("""Below are the rules of the game:
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
        you will both get another turn until the tie is broken.""")
    print("\nThe Game is starting....")

def human_move(computer_score, human_score):
    """This function displays a player's and the computer's current
    score, and how far behind (or ahead) the player is. Then repeatedly
    asks whether the player wants to roll again. This continues until either:
    -   The player decides not to roll again. The function returns the
        total of the rolls made during this move.
    -   The player rolls a 1. The function returns 0.
    Arguments (Type):= current computer and human scores (*integer*).
    """

    sum_of_rolls = 0
    prompt = "Roll die again? 'Y' or 'N':"

    print("Current scores:", "You =", human_score,  # print current score
          "| Computer =", computer_score)
    print(compare_scores(computer_score, human_score))

    while True:  # Asks whether player wants to roll again
        if ask_yes_or_no(prompt):
            this_roll = roll()
            if this_roll == 1:
                return 0
            else:
                sum_of_rolls += this_roll
        else:
            return sum_of_rolls

def compare_scores(computer_score, human_score):
    """This funcion constructs a comparison between the current human
    and computer_score and returns a string value.
    Arguments (Type):= current computer and human scores (*integer*).
    """

    score_diff = human_score - computer_score
    if score_diff > 0:
        return "You are " + str(abs(score_diff)) + " AHEAD of the Computer"
    elif score_diff < 0:
        return "You are " + str(abs(score_diff)) + " BEHIND the Computer"
    else:
        return "You are level with the Computer at " + str(human_score)

def computer_move(computer_score, human_score):
    """This function computes the computer rolls some number of times,
    displays the result of each roll, and the function returns the
    result (either 0 or the total of the rolls). The function uses an
    algorithim  to determine frequency of play: `gently` when computer
    is ahead and agressively if it is behind.
    Arguments (Type):= current computer and human scores (*integer*).
    """

    total_of_rolls = 0
    aggressive = 5
    gently = 2

    if computer_score - human_score <= 0: # Computer selects play style
        style = aggressive
    else:
        style = gently

    for i in range(1, 1 + style):
        this_roll = roll()
        print("Computer roll:", i, "number =", this_roll)
        if this_roll == 1:
            return 0
        else:
            total_of_rolls += this_roll
    return total_of_rolls

def is_game_over(computer_score, human_score):
    """Returns `True` if either player has 100 or more, and the players
    are not tied, otherwise it returns `False`. Called  only after
    the human player's move.
    Arguments (Type):= current computer and human scores (*integer*).
    """

    return ((computer_score >= 100 or human_score >= 100)
            and computer_score != human_score)

def roll():
    """Returns a random number in the range 1 to 6"""
    from random import randint
    return randint(1, 6)

def ask_yes_or_no(prompt):
    """Prints the prompt as a question to the player. Returns `True`
    if player responds with a string with first character `'y'` or `'Y'`,
    returns `False` if first character of player response is `'n'` or `'N'`
    else repeats question until the player provides an acceptable response.
    """

    response = input(prompt)
    try:
        if response[0] in {"Y", "y"}:
            return True
        elif response[0] in {'N', 'n'}:
            return False
        else:
            return ask_yes_or_no(prompt)
    except IndexError:
        return ask_yes_or_no(prompt)

def show_results(computer_score, human_score):
    """Function is called when the game has ended to tell
    whether the human player won or lost, and by how much.
    Arguments (Type):= current computer and human scores (*integer*).
    """

    if computer_score > human_score:
        print("\nGame Over!! You LOST by: "
              + str(computer_score - human_score))
    else:
        print("\nGame Over!! You WON by: "
              + str(human_score - computer_score))

if __name__ == '__main__':
    main()
