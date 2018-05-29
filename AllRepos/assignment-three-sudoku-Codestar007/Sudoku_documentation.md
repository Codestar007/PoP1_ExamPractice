Help on module sudoku:

NAME
    sudoku

DESCRIPTION
    Name:  Kizito Jegede
    ID: Codestar007
    Course: MSc CS - PoP 1
    
    Assignment Three: (Please refer to 'README.dm' for full despecificationt)
    Program Title: Sudoku
    Program Description:    In Sudoku, a player is given a 9x9 grid, divided
                            into nine 3x3 "boxes,". Each box has nine "cells,"
                            and some of these cells have digits in them
                            (but most are blank). The puzzle is to fill in the
                            rest of the grid so that every row, every column,
                            and every 3x3 box contains the digits 1 through 9.

FUNCTIONS
    convertToInts(problem)
        Function takes as a parameter, a two-dimensional array `problem`
        of sets, create and return a new two-dimensional array of integers.
        For each location in `problem` that contains a singleton set, the
        corresponding integer array location contains that one element. For
        each location in `problem` that contains a set with more than one
        element or empty set, the corresponding location in the result array
        is set to zero.
    
    convertToSets(problem)
        Given a two-dimensional array *`problem`* of integers, create and
        return a new two-dimensional array of sets.
    
    eliminate(problem, location, listOfLocations)
        The given `location` in the array *`problem`* should contain a set
        containing a single number. For each location in
        the *`listOfLocations`* **except* `location`***, remove the number
        in *`location`* from the set in each other location. This
        function **changes the array** *`problem`* and returns a count of
        the number of eliminations (removals) actually made.
    
    elimination_calls(problem, location, listOfLocations)
        called `eliminate` with row, column, and box locations.
        Returns true or false.
    
    getBoxLocations(location)
        Return a list of all nine "locations"  (`(row, column)`  tuples) in
        the same box as the given `location`.
    
    getColumnLocations(columnNumber)
        Given a `columnNumber`, return a list of all nine "locations" 
        (`(row, column)`  tuples) in that column.
    
    getRowLocations(rowNumber)
        Given a `rowNumber`, return a list of all nine "locations" 
        (`(row, column)`  tuples) in that row.
    
    isSolved(problem)
        Given a two-dimensional array `problem` of sets, return `True` if
        the Sudoku problem has been solved (every set contains exactly one
        element), and `False` otherwise.
    
    main()
        Ask the user for the name of a file containing a Sudoku puzzle.
        Print the puzzle, try to solve the puzzle, then print the (possibly
        incomplete) solution. If the puzzle has not been completely solved,
        then also print out a list of unsolved locations, and what numbers
        are still possible for those locations. After each solution, ask
        the user if s/he wants to read in and solve another puzzle.
    
    print_beam(bx_col)
        Takes an intiger arguments and prints grid bars for
        sudoku problems and solution.
    
    print_post(col, g_cols)
        Takes 2 intiger arguments and prints grid posts for
        sudoku problems and solution.
    
    print_sudoku(problem)
        Prints the Sudoku array (given as a list of lists of integers),
        using dots to represent zeros.
    
    print_unsolved(problem)
        Given a two-dimensional array `problem` of sets,
        prints out a list of unsolved locations and possible numbers.
    
    read_sudoku(file)
        Reads and returns in a Sudoku problem from a file.
    
    solve(problem)
        Given a two-dimensional array `problem` of sets, try to solve it.
        This function **changes the array** *`problem`* and
        returns `True` if the problem has been solved, `False` otherwise.
    
    solveAnotherPuzzle(prompt)
        After each solution, the user is asked if s/he wants to read in
        and solve another puzzle. Returns `True` If the player
        responds with a string whose first character is `'y'` or `'Y'`,
        and `False` if the player responds with a string whose first
        character is `'n'` or `'N'`. Handles  'IndexError' exception.

FILE
    assignment-three-sudoku-codestar007/sudoku.py


