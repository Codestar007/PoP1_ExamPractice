"""
Name:  Kizito Jegede
ID: Codestar007
Course: MSc CS - PoP 1

Assignment Three: (Please refer to 'README.dm' for full despecificationt)
Program Title: Sudoku
Program Description:    In Sudoku, a player is given a 9x9 grid, divided
                        into nine 3x3 "boxes,". Each box has nine "cells,"
                        and some of these cells have digits in them
                        (but most are blank). The puzzle is to fill in the
                        rest of the grid so that every row, every column,
                        and every 3x3 box contains the digits 1 through 9.
"""

import copy
import math

def main():
    """Ask the user for the name of a file containing a Sudoku puzzle.
    Print the puzzle, try to solve the puzzle, then print the (possibly
    incomplete) solution. If the puzzle has not been completely solved,
    then also print out a list of unsolved locations, and what numbers
    are still possible for those locations. After each solution, ask
    the user if s/he wants to read in and solve another puzzle.
    """

    #Ask player the name of a file containing a Sudoku puzzle
    probFile = input("Provide name of file containing a Sudoku puzzle: ")
    problem = read_sudoku(probFile)
    print("Sudoku Problem:")
    print_sudoku(problem)
    problemSet = convertToSets(problem)

    if solve(problemSet):
        print("\nProblem Solution:")
        print_sudoku(convertToInts(problemSet))
    else:
        print("\nIncomplete Solution:")
        print_sudoku(convertToInts(problemSet))
        print_unsolved(problemSet)

    if solveAnotherPuzzle("\nRead in and solve another puzzle (y / n):"):
        main() # Play again

def read_sudoku(file):
    """Reads and returns in a Sudoku problem from a file."""
    stream = open(file)
    data = stream.readlines()
    stream.close()
    return eval("".join(data))

def convertToSets(problem):
    """Given a two-dimensional array *`problem`* of integers, create and
    return a new two-dimensional array of sets.
    """
    problem_copy = copy.deepcopy(problem)
    g_rows = len(problem_copy)  # number of rows
    g_cols = len(problem_copy[0])  # number of colums

    for row in range(g_rows):
        for col in range(g_cols):
            if problem_copy[row][col] == 0:
                problem_copy[row][col] = {int(i) for i in range(1, len(problem_copy) + 1)}
            else:
                problem_copy[row][col] = {problem_copy[row][col]}
    return problem_copy

def convertToInts(problem):
    """Takes as a parameter, a two-dimensional array `problem`
    of sets, create and return a new two-dimensional array of integers.
    For each location in `problem` that contains a singleton set, the
    corresponding integer array location contains that one element. For
    each location in `problem` that contains a set with more than one
    element or empty set, the corresponding location in the result array
    is set to zero.
    """

    problem_copy = copy.deepcopy(problem)
    g_rows = len(problem_copy)  # number of rows
    g_cols = len(problem_copy[0])  # number of colums

    for row in range(g_rows):
        for col in range(g_cols):
            if len(problem_copy[row][col]) > 1 or len(problem_copy[row][col]) == 0:
                problem_copy[row][col] = 0
            else:
                convSet = (int(i) for i in problem_copy[row][col]) # Convert singleton to intiger
                for elem in convSet: problem_copy[row][col] = elem
    return problem_copy

def getRowLocations(rowNumber):
    """Given a `rowNumber`, return a list of all nine "locations" 
    (`(row, column)`  tuples) in that row.
    """

    newLst = [(rowNumber, i) for i in range(9)]
    return newLst

def getColumnLocations(columnNumber):
    """Given a `columnNumber`, return a list of all nine "locations" 
    (`(row, column)`  tuples) in that column.
    """

    newLst = [(i, columnNumber) for i in range(9)]
    return newLst

def getBoxLocations(location):
    """Return a list of all nine "locations"  (`(row, column)`  tuples)
     in the same box as the given `location`.
    """
    location_list = []
    row, col = location
    box_start_coords = [(x, y) for x in range(0, 9, 3) for y in range(0, 9, 3)]
    for elem in box_start_coords:
        if row <= elem[0] + 2 and row >= elem[0] and col <= elem[1] + 2 and col >= elem[1]:
            x_cord, y_cord = elem
            location_list = [(x, y) for x in range(x_cord, x_cord + 3)
                             for y in range(y_cord, y_cord + 3)]
            return location_list

def eliminate(problem, location, listOfLocations):
    """The given `location` in the array *`problem`* should contain
     a set containing a single number. For each location in
    the *`listOfLocations`* **except* `location`***, remove the number
    in *`location`* from the set in each other location. This
    function **changes the array** *`problem`* and returns a count of
    the number of eliminations (removals) actually made.
    """

    count = 0
    r, c = location  # row and colum ref
    loc_value = list(problem[r][c])[0]

    for loc in listOfLocations:
        row, col = loc
        if loc_value in problem[row][col] and location != loc:
            problem[row][col].remove(loc_value) # From the other set locations
            count += 1
    return count

def isSolved(problem):
    """Given a two-dimensional array `problem` of sets, return `True` if
    the Sudoku problem has been solved (every set contains exactly one
    element), and `False` otherwise.
    """

    g_rows = len(problem)  # number of rows
    g_cols = len(problem[0])  # number of colums

    if all([len(problem[row][col]) == 1 for row in range(0, g_rows)
            for col in range(0, g_cols)]): return True
    else: return False

def solve(problem):
    """Given a two-dimensional array `problem` of sets, try to solve it.
    This function **changes the array** *`problem`* and
    returns `True` if the problem has been solved, `False` otherwise,
    for every location in the array, call `eliminate` with row, column, 
    and box locations. If any values have been eliminated 
    (`eliminate` returns something other than zero), repeat this procedure. 
    When it is no longer possible to eliminate anything, return the boolean result.
    """

    g_rows = len(problem)  # number of rows
    g_cols = len(problem[0])  # number of colums
    elimCount = 0 # count of numbers eliminated
    for row in range(g_rows):
        for col in range(g_cols):
            if len(problem[row][col]) == 1: # if "singleton" set
                # call `eliminate` with row, column and Boxlocations in turn
                elimCount += elimination_calls(problem, (row, col),
                                               getRowLocations(row))
                elimCount += elimination_calls(problem, (row, col),
                                               getColumnLocations(col))
                elimCount += elimination_calls(problem, (row, col),
                                               getBoxLocations((row, col)))
    if elimCount > 0: solve(problem) # Recurssion
    return isSolved(problem)

def print_unsolved(problem):
    """Given a two-dimensional array `problem` of sets,
    prints out a list of unsolved locations and possible numbers.
    """

    g_rows = len(problem)  # number of rows
    g_cols = len(problem[0])  # number of colums

    print("\nUnsolved  :  Possible")
    print("Location  :  Numbers")
    unsolved = [str((row, col)) + (" " * 4) + ":  "
                + str(problem[row][col]) for row in
                range(0, g_rows) for col in range(0, g_cols)
                if len(problem[row][col]) > 1]

    for elem in unsolved:
        print(elem)

def elimination_calls(problem, location, listOfLocations):
    """called `eliminate` with row, column, and box locations.
    Returns true or false.
    """
    
    thiscount = 0
    for loc in listOfLocations:
        thiscount += eliminate(problem, location, listOfLocations)
    return thiscount > 0

def print_sudoku(problem):
    """Prints the Sudoku array (given as a list of lists of integers),
    using dots to represent zeros.
    """

    g_rows, g_cols = len(problem), len(problem) #9, 9  # Grid dimenssions
    bx_rw, bx_col = math.sqrt(len(problem)), math.sqrt(len(problem))  # 3, 3  # Box dimenssions
    beam_multiplier = int(math.sqrt(len(problem)))

    print_beam(bx_col, beam_multiplier) # Print Topmost Gridbeam
    for row in range(g_rows):
        for col in range(g_cols):
            if col == 0: print_post(col, g_cols) # Print post
            if problem[row][col] == 0:
                print(".", end=' ') # Print box/grid values
            else:
                print(problem[row][col], end=' ') # Print box/grid values
            if ((col + 1) % bx_col) == 0: print_post(col, g_cols) # Print post
        if (row + 1) % bx_rw == 0:
            print_beam(bx_col, beam_multiplier) # Print Grid or box beam

def print_beam(bx_col, beam_multiplier):
    """Takes an intiger arguments and prints grid bars for
    sudoku problems and solution.
    """

    print((('+-' + ('--' * beam_multiplier)) * int(bx_col)) + '+')


def print_post(col, g_cols):
    """Takes 2 intiger arguments and prints grid posts for
    sudoku problems and solution.
    """

    if col + 1 == g_cols:
        print('|')
    else:
        print('|', end=' ')

def solveAnotherPuzzle(prompt):
    """After each solution, the user is asked if s/he wants to read in
    and solve another puzzle. Returns `True` If the player
    responds with a string whose first character is `'y'` or `'Y'`,
    and `False` if the player responds with a string whose first
    character is `'n'` or `'N'`. Handles  'IndexError' exception.
    """

    response = input(prompt)
    try:
        if response[0]  in {"Y", "y"}:
            return True
        elif response[0]  in {"N", "n"}:
            return False
        else:
            return solveAnotherPuzzle(prompt)
    except IndexError:
        return solveAnotherPuzzle(prompt)


if __name__ == '__main__':
    main()
