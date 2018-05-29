"""
Name:  Kizito Jegede
ID: Codestar007
Course: MSc CS - PoP 1

Assignment One: (Please refer to 'README.dm' for full details)
Program Title: Lunar Lander
Program Description: An interactive game that takes inputs from a
                     player in order to control and  safely land a
                     lunar module on the Moon's surface.
"""


def calc_fuel_burn_adjustment(fuel_burn, fuel_bal):
    """This function calculates any required adjustments to fuel burn
    after user response to request for quantity of fuel to burn.
    - Arguments:= *float* - fuel to burn and current fuel balance.
    - Return value type:= *float*.
    """

    if fuel_burn > fuel_bal:
        fuel_burn = fuel_bal
    elif fuel_burn < 0.0:
        fuel_burn = 0.0
    return fuel_burn


def fuel_input_and_valid(turn):
    """This function asks a player to input (integer or float)
    quantity of fuel to burn and validates the entry. It  will
    recurse if the player enters invalid entry e.g string.
    - Arguments:= *integer* - current turn.
    - Return value type:= *float*.
    - Exception caught:= ValueError
    """

    try:
        fuel_burn = float(input("\nTurn: " + str(turn)
                                + " - How much fuel do you want to burn? "
                                + "e.g 12 or 3.45: "))
        return fuel_burn
    except ValueError:
        return fuel_input_and_valid(turn)


def calc_fuel_balance(fuel_burn, fuel_bal):
    """Function called to calculate fuel balance after every fuel burn.
    - Arguments:= *float* - fuel burnt and current fuel balance.
    - Return value type:= *float*.
    """

    if fuel_burn > fuel_bal:
        fuel_bal = 0.0
    else:
        fuel_bal -= fuel_burn

    return fuel_bal


def calc_velocity(velocity, fuel_burn, v_const):
    """This function calculates the velocity after every fuel burn.
    - Arguments:= *float* - current velocity, fuel burnt and a constant.
    - Return value type:= *float*.
    """

    velocity += (1.6 - (v_const * fuel_burn))
    return velocity


def calc_altitude(altitude, velocity):
    """This function is called to calculate altitude after every
    fuel burn.
    - Arguments:= *float* - current altitude and velocity.
    - Return value type:= *float*.
    """

    altitude -= velocity
    return altitude


def print_dashboard_values(velocity, altitude, fuel_bal):
    """This function prints out the value of velocity, altitude,
    fuel balance at each turn.The velocity and altitude values are
    rounded to 2 decimal places before printing.
    - Arguments:= *float* - current velocity, altitude and fuel balance.
    """

    print("Velocity:", "%.2f" % velocity, "metres/sec.",
          "\nAltitude:", "%.2f" % altitude, "metres",
          "\nFuel balance:", fuel_bal, "litres")


def q_has_module_landed(altitude, velocity):
    """This function checks if the module has landed safely or crashed.
    - Arguments:= *float* - current altitude and velocity.
    - Return value type:= *string*.
    """

    if altitude <= 0.0 and velocity <= 10.0:
        return "Landed"
    elif altitude <= 0.0 and velocity > 10.0:
        return "Crashed"


def printout_landing_msg(altitude, velocity, fuel_bal,
                         total_turns, landing_status):
    """Function prints out the message after the LunarLander has landed.
    The velocity and altitude values are rounded to 2 decimal places
    before printing.
    - Arguments:= *float* - current altitude, velocity, fuel balance.
                  *integer* - total turns in the game.
                  *string* - landing status
    """
    if landing_status == "Landed":
        print("\nCONGRATULATIONS! You SAFELY landed the Lunar Module in"
              + " " + str(total_turns) + " Secs.")
        print("\nFINAL LUNAR LANDER DASHBOARD NUMBERS:\n"
              + "-" * 36
              + "\nAltitude: " + str("%.2f" % altitude)
              + "\nVelocity: " + str("%.2f" % velocity)
              + "\nFuel balance: " + str(fuel_bal) + "\n"
              + "=" * 36 + "\n")
    elif landing_status == "Crashed":
        # noinspection SpellCheckingInspection
        print("\n" + "-" * 47
              + "\nOoops! You have CRASH LANDED the Lunar Module!!\n"
              + "Depth of crater:", "%.2f" % velocity, "metres\n"
              + "=" * 47 + "\n")


def q_play_again(prompt):
    """This function prompts the player to confirm if they want to repeat
    the Game. Requires a yes or no response. input request will recurse
    if the player enters invalid entry (e.g. return without data).
    - Arguments:= *string* - input prompt.
    - Return value type:= *boolean*.
    - Exception caught:= IndexError.
    """

    response = input(prompt)
    try:
        if response.startswith('Y') or response.startswith('y'):
            return True
        elif response.startswith('N') or response.startswith('n'):
            return False
        else:
            return q_play_again(prompt)
    except IndexError:
        return q_play_again(prompt)


def main():
    """Main module to begin the game and and call various functions
    to calculate the LunarLander's position and print out the game
    status. It takes no arguments.
    """

    finished = False
    fuel_bal = 1000.0
    velocity = 0.0
    altitude = 1000.0
    v_const = 0.15
    total_turns = 0
    fuel_input = 0.0
    fuel_burn = 0.0
    landing_status = ""

    while not finished:
        while altitude > 0.0:
            total_turns += 1
            if total_turns > 1:
                # get fuel burn input from player, adjust the value if required
                fuel_input = fuel_input_and_valid(total_turns)
                fuel_burn = calc_fuel_burn_adjustment(
                    fuel_input, fuel_bal)
            else:
                print("\nTurn:", total_turns)  # prints for turn 1 only

            # Get lander dashboard values and print out the values
            fuel_bal = calc_fuel_balance(fuel_burn, fuel_bal)
            velocity = calc_velocity(velocity, fuel_burn, v_const)
            altitude = calc_altitude(altitude, velocity)
            print_dashboard_values(velocity, altitude, fuel_bal)

            # Check if Lander has landed
            landing_status = q_has_module_landed(altitude, velocity)
            if landing_status == "Crashed" or landing_status == "Landed":
                printout_landing_msg(
                    0.0, velocity, fuel_bal,
                    total_turns, landing_status)

        # Check if player wants to play again
        if q_play_again("Do you want to play again? (Yes or No): "):
            finished = True
            main()
        else:
            finished = True
            print("\nEND of GAME!!!")


if __name__ == '__main__':
    main()
