
import BlueConnect as blueconnect
import LEDGrid as matrix
import IPLocal as ip
import GaussianEliminationSolver as fastSolve
import Backtracker as slowSolve

from random import randint, shuffle
import time

# a matrix that represembles the bluetooth symbol
bluetoothImage = [
    [0,0,0,0,0,0,0,0],
    [0,1,0,0,0,0,1,0],
    [0,0,1,0,0,1,0,0],
    [1,1,1,1,1,1,1,1],
    [0,1,0,1,1,0,1,0],
    [0,0,1,0,0,1,0,0],
    [0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0]
]

# a matrix that resembles the wifi symbol
wifiImage = [
    [0,1,0,0,1,0,0,0],
    [1,0,0,1,0,0,1,0],
    [1,0,1,0,0,1,0,0],
    [1,0,1,0,1,0,0,1],
    [1,0,1,0,1,0,0,1],
    [1,0,1,0,0,1,0,0],
    [1,0,0,1,0,0,1,0],
    [0,1,0,0,1,0,0,0]
]

# an Adapter function that converts a 4x4 matrix to display on our 8x8 LED Matrix Display
def convert4to8Board(game4Array):
    temp = [[0 for x in range(8)] for y in range(8)]
    for row in range(4):
        for col in range(4):
            trow = (row * 2)
            tcol = (col * 2)
            temp[trow][tcol] = game4Array[row][col]
            temp[trow][tcol + 1] = game4Array[row][col]
            temp[trow + 1][tcol] = game4Array[row][col]
            temp[trow + 1][tcol + 1] = game4Array[row][col]

    return temp

# prints array to the LED display, with game4 being a
# boolean, true for 4x4 and false for 8x8.
def printToBoard(array, game4):
    if(game4 == True):
        matrix.printScreen(convert4to8Board(array))
    else:
        matrix.printScreen(array)

# randomizes the state of the board by making
# random moves
def randomize(array):
    x = randint(0, len(array) - 1)
    y = randint(0, len(array[x]) - 1)
    return move(x,y,array)

# outputs a boolean of whether the player has won a board
def hasWon(board):
    won = True
    for row in range(len(board)):
        for col in range(len(board[row])):
            if(board[row][col] == 0):
                won = False
    return won

# checks if the x and y positions are valid for the board
def checkValid(x, y, game_board):
    return (x >= 0 and x < len(game_board)) and (y >= 0 and y < len(game_board[0]))

# negates the state of a tile on the board
def negate(input):
    if(input == 1):
        return 0
    else:
        return 1

# represents a move on the board
def move(x, y, game_board):
    if checkValid(x, y, game_board): game_board[x][y] = negate(game_board[x][y])
    if checkValid(x, y-1, game_board): game_board[x][y-1] = negate(game_board[x][y-1])
    if checkValid(x, y+1, game_board): game_board[x][y+1] = negate(game_board[x][y+1])
    if checkValid(x-1, y, game_board): game_board[x-1][y] = negate(game_board[x-1][y])
    if checkValid(x+1, y, game_board): game_board[x+1][y] = negate(game_board[x+1][y])
    return game_board

# this is used by the backtracker to display the board
# to the LED Display. Used to be used to sleep the display
def backTrackingDisplay(game_board, play4):
    printToBoard(game_board, play4)

# main function
if __name__ == '__main__':

    # the board starts looking for wifi.
    isConnected = False
    printToBoard(wifiImage, False)

    # for debugging
    if(ip.connected_to_internet()):
        isConnected = True
    else:
        time.sleep(10)
        if(ip.connected_to_internet()):
            isConnected = True

    # prints the ip address
    if(isConnected == True):
        matrix.print_message(ip.get_ip_address('wlan0'))

    # prints the bluetooth image now that the board is connected
    printToBoard(bluetoothImage, False)

    blueconnect.wait_for_connect()

    matrix.print_message("Connected")

    # used to have the person choose the size of the board
    while(True):
        choose = blueconnect.getNext()
        print(choose)
        if(choose == "4"):
            play4 = True
            matrix.print_message("4x4")

        else:
            play4 = False
            matrix.print_message("8x8")

    # starting game
        if(play4):
            c, r = 4, 4
        else:
            c, r = 8, 8

        # initialize game board
        game_board = [[1 for x in range(c)] for y in range(r)]

        # randomize game board
        for times in range(0, 30):
            for steps in range(0, 4):
                game_board = randomize(game_board)
            printToBoard(game_board, play4)
            time.sleep(0.05)

        # wait for player move, main loop of game
        input = ""
        while hasWon(game_board) == False:

            input = blueconnect.getNext()

            # fast and slow are solvers, and they always bring the game
            # to a winning state
            if input == "fast" or input == "slow":
                break

            # get the input for a move
            inputArray = input.split(",")
            print(inputArray)
            x = int(inputArray[1])
            y = int(inputArray[0])
            game_board = move(x, y, game_board)
            printToBoard(game_board, play4)

        # solve using Gaussian Elimination
        if input == "fast":
            # gets a list of the steps to victory
            movesToVictory = fastSolve.solveGaussianElimination(game_board)

            # randomize to make it look more magical
            shuffle(movesToVictory)

            # execute all the steps in movesToVictory,
            # displaying them for 5 seconds each
            for position in movesToVictory:
                game_board = move(position[0], position[1], game_board)
                printToBoard(game_board, play4)
                time.sleep(0.5)

        # solve using Backtracking
        elif input == "slow":
            slowSolve.solveBacktracking(game_board, play4)

        # this makes the display flash on and off
        # indicates victory
        for i in range(11):
            matrix.invert(i%2)
            time.sleep(0.2)

        matrix.print_message("Winner")