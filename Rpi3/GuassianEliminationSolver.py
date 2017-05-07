__author__ = 'Curti_000'

# Author: Curtis Shea (cgs8601), based on work of Paul Hankin
# Filename: Solver.java
# Date (created): 5/6/2017
# Used for solving a LightsOn board quickly

# Code from Paul Hankin was  used for the solve method.
# Comments were added, and variable names were tweaked.
# The code can be found on StackOverflow at this URL:
# http://stackoverflow.com/questions/7212966/any-algorithm-for-flip-all-light-out-game

# I understand exactly what the code and algorithm does, but I do not,
# as of the time of this writing, understand why it works. I'll research it
# later, since this is interesting. If I knew how it worked I would have
# made it look to get 1's for state instead of 0's. Currently I just used a kludgy
# fix of inverting the state of the inputted board. It does work though.

# solves a board of any dimension, taking in a board of int[row][col]
# outputs a list of tuples of x,y coordinates
def solveGuassianElimination(board):
    rowSize, colSize = len(board), len(board[0])
    eqs = []

    board = list(board)

    # negate all board values, since algorithm works for finding moves to Lights Out
    for row in range(rowSize):
        for col in range(colSize):
            if board[row][col] == 0:
                board[row][col] = 1
            else:
                board[row][col] = 0


    # sets up the equations representing the initial state of the board
    # using modulo 2 aritmetic. There is one equation per tile,
    # and the tile is represented by possible moves from adjacent tiles (including self)
    for row in range(rowSize):
        for col in range(colSize):
            eq = set()
            # gets tiles adjacent to current, including current. Adds them to equation
            for offset in range(-1, 2):
                if 0 <= row+offset < rowSize:
                    eq.add((row+offset)*colSize+col)
                if offset != 0 and 0 <= col+offset < colSize:
                    eq.add(row*colSize+col+offset)
            # stores as an array of objects that each have an a and the equation representing the a value
            eqs.append([board[row][col], eq])


    numEQs = len(eqs)

    for i in range(numEQs):
        # converts all equations to be E equations that are used to eliminate
        # a tile as a possible move from all but that equation
        for j in range(i, numEQs):
            #gets the equations
            if i in eqs[j][1]:
                # reverses the storage of the equations.
                # Used to sort E equations to top so that they are never accessed
                eqs[i], eqs[j] = eqs[j], eqs[i]
                break #break past assigning equations

        # XOR (modulo 2 aritmetic) the E equation and any equations that
        # contain the tile that the E equation is for, this eliminates that
        # tile from all other equations
        for j in range(i+1, numEQs):
            if i in eqs[j][1]:
                # state is added as well
                eqs[j][0] ^= eqs[i][0]
                eqs[j][1] ^= eqs[i][1]

    # Once all E equations have been made, go through and finally solve
    # for state resulting from a move
    # at the end, each E equation will have only one possible move to represent it's
    # a value, and the a value will only be 1 if it contributes to the list of winning moves
    # for a board. #MAGIC (with numbers)
    for i in range(numEQs-1, -1, -1):
        for j in range(i):
            if i in eqs[j][1]:
                # add a-value and x-value that represents equation
                eqs[j][0] ^= eqs[i][0]
                eqs[j][1] ^= eqs[i][1]

    # convert the raw moves to a list of coordinates
    return [(i//colSize,i%colSize) for i, eq in enumerate(eqs) if  eq[0]]



if __name__ == '__main__':
    print(solveGuassianElimination(([1, 0, 0], [0, 1, 0], [0, 0, 1], [0, 0, 0])))
