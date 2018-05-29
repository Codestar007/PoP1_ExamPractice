'''
Name:  Kizito Jegede
ID: Codestar007
Course: MSc CS - PoP 1

Assignment One: (Please refer to 'README.dm' for full details)
Program Title: Hundred 
Program Description: An interactive game where two players takes turns to roll a dice. At the end of each turn,
                    the score for that turn is added to the player's total score. The first player to reach or exceed 100 wins..'''


def main():
    '''This is where your program will start execution.'''
    print("Game starting....")
    computer_score = None
    human_scr = None
    
def instructions():
    '''Tell the user the rules of the game.'''
    print('''Below are the rules of the game:
    1. Two players take turns; The computer always goes first
    2. On each turn, a player rolls a six-sided die as many times as she wishes, or until she rolls a 1.
    3. Each number she rolls, except a 1, is added to her score this turn.
    4. But if she rolls a 1, her score for this turn is zero, and her turn ends.
    5. At the end of each turn,the score for that turn is added to the player's total score.
    6. The first player to reach or exceed 100 wins.
    7. if the *first* player reaches or exceeds 100, the second player gets one additional turn.
    8. If both players are tied with 100 or more, each gets another turn until
    the tie is broken''')

def human_move(computer_score):
    '''Tells the user both her current score and the computer's score, and how
    far behind (or ahead) she is. Then repeatedly asks whether the user
    wants to roll again. This continues until either:

    -   The user decides not to roll again. The function should return the
        total of the rolls made during this move.
    -   The user rolls a 1. The function should return 0.'''

def computer_move(computer_score):
    '''The computer rolls some number of times, displays the result of each
    roll, and the function returns the result (either 0 or the total of
    the rolls). The function may use its parameters in order to play
    more intelligently (for example, it may wish to gamble more
    agressively if it is behind).'''

def is_game_over(computer_score):
    '''Returns `True` if either player has 100 or more, and the players are
    not tied, otherwise it returns `False`. (Call this  only after the
    human's move.)'''

def roll():
    '''Returns a random number in the range 1 to 6, inclusive. To do this,
    find the `random` module
    on <https://docs.python.org/3/library/index.html> and follow the
    link to find the `randint` method.'''
    from random import randint
    return randint(1, 6)
    #print(s)
    
def ask_yes_or_no(prompt):
    '''Prints the prompt as a question to the user, for
    example, `"Roll again? "`. If the user responds with a string whose
    first character is `'y'` or `'Y'`, the function returns `True`. If
    the user responds with a string whose first character
    is `'n'` or `'N'`, the function returns `False`. Any other response
    will cause the question to be repeated until the user provides an
    acceptable response.'''
    response = input(prompt)
    if response[0] == "Y" or response[0] == "y":
        return "Yes"
    if response[0] == 'N' or response[0] == 'n':
        return "No" 
    else:
        ask_yes_or_no(prompt)

def show_results(computer_score):
    '''Tells whether the human won or lost, and by how much. (Call this
    when the game has ended.)'''

main()
print("\n")
instructions()
