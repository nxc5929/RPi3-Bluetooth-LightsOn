import BlueConnect as blueconnect
import LEDGrid as matrix
from random import randint
import time


def gameToBoard(game4Array):
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


blueconnect.wait_for_connect()

play4 = True

matrix.print_message("Starting the game")
if(play4):
    c, r = 4, 4
    gameboard = [[0 for x in range(c)] for y in range(r)]
    for times in range(0, 30):
        for row in range(r):
            for col in range(c):
                gameboard[row][col] = randint(0, 1)
        matrix.printScreen(gameToBoard(gameboard))
        time.sleep(0.05)

else:
    c, r = 8, 8
    gameboard = [[0 for x in range(c)] for y in range(r)]
    for times in range(0, 30):
        for row in range(r):
            for col in range(c):
                gameboard[row][col] = randint(0, 1)
        matrix.printScreen(gameboard)
        time.sleep(0.05)