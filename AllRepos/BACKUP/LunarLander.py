'''
Name:  Kizito Jegede
ID: Codestar007
Course: MSc CS - PoP 1

Assignment One: (Please refer to 'README.dm' for full details)
Program Title: Lunar Lander 
Program Description: An interactive game that takes inputs from a player 
                     in order to control and  safely land a lunar module on the Moon's surface.'''


def calc_lunar_position():
    ''' This function contain the main game calculations and runs the loop calls 2 other function - 
        2) To ask if the player would like to replay the game. 1) to validate the user fuel burn input.'''
        
    altitude = 1000.0
    velocity = 0.0
    fuel_bal = 1000.0
    first_turn = True
    const_s = 0.15
    turn = 0

    data_entry_string = "0"

    while altitude != 0.0 or altitude > 0.0:

        if first_turn: 
            turn = 1
            fuel_burn = 0.0
            velocity += 1.6
            first_turn = False

        else:
            turn += 1
            fuel_burn = input_valid(turn) # float(input("How much fuel do you want to burn?"))
            data_entry_string = data_entry_string + "," + str(fuel_burn)

            # calculate fuel burn and fuel balance
            if fuel_burn > fuel_bal:
                fuel_burn, fuel_bal = fuel_bal, 0.0
                #fuel_bal = 0.0
            elif fuel_burn < 0.0:
                fuel_burn = 0.0
            else:
                fuel_bal -= fuel_burn
            print("fuel_burn: ", fuel_burn)
            print("fuel_bal: ", fuel_bal)
            
            # calculate change in velocity      
            velocity += (1.6 - (const_s * fuel_burn))
            print("velocity: ", velocity)

        # calculate change in altitude
        altitude -= velocity
        print("altitude: ", altitude)

        # determine if palunar Module has landed and safely
        if altitude <= 0.0:
            if velocity <= 10.0:
                altitude = 0.0

                print("CONGRATULATIONS!! You have SAFELY landed the Lunar Module on the Moon's surface in " + str(turn) + " seconds.")
                print("Final numbers: -","altitude:", altitude,"velocity:", velocity,"fuel balance:", fuel_bal)
                print("Winning inputs: ", data_entry_string)
                
                # Check if player wants to play again
                if q_play_again() == "Yes":
                    calc_lunar_position()
                else:
                    print("END of GAME!!!")

            else:
                altitude = 0.0
                print("Ooops! CRASH LANDED!! Depth of crater:", velocity)
                print("Loosing inputs: ", data_entry_string)

                # Check if player wants to play again
                if q_play_again() == "Yes":
                    calc_lunar_position()
                else:
                    print("END of GAME!!!")

def q_play_again():
    ''' This function promts the palyer to confirm if they want to repeat the Game. 
        It  will recurse if the player enters invalid entry. It returns a Boolean value.'''

    response = input("Do you want to play again? Answer Yes or No: ")
    if response[0] == "Y" or response[0] == "y":
        return "Yes"
    if response[0] == 'N' or response[0] == 'n':
        return "No" 
    else:
        return q_play_again()

def input_valid(turn_t): # validate user input is float or intiger
    ''' This function takes an intiger or float entry (fuel burn) and validates the entry. 
        It  will recurse if the player enters invalid entry e.g string. It returns a float number.'''

    resp = input("Turn:" + str(turn_t) + " - How much fuel to burn? Enter number e.g 12 or 3.45: ")
    
    try:
        return float(resp)
    except ValueError:
        return input_valid(turn_t) # ask player for a valid input

calc_lunar_position()

