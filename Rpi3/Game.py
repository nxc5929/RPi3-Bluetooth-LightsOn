import BlueConnect as blueconnect
import LEDGrid as matrix
from random import randint
import time

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

def printToBoard(array, game4):
    if(game4 == True):
        matrix.printScreen(convert4to8Board(array))
    else:
        matrix.printScreen(array)

def randomize(array):
    for row in range(len(array)):
        for col in range(len(array[row])):
            array[row][col] = randint(0, 1)
    return array

def hasWon(board):
    won = True
    for row in range(len(board)):
        for col in range(len(board[row])):
            if(board[row][col] == 0):
                won = False
    return won

def checkValid(x, y, game_board):
    return (x >= 0 and x < len(game_board)) and (y >= 0 and y < len(game_board[0]))

def negate(input):
    if(input == 1):
        return 0
    else:
        return 1

def move(x, y, game_board):
    if checkValid(x, y, game_board): game_board[x][y] = negate(game_board[x][y])
    if checkValid(x, y-1, game_board): game_board[x][y-1] = negate(game_board[x][y-1])
    if checkValid(x, y+1, game_board): game_board[x][y+1] = negate(game_board[x][y+1])
    if checkValid(x-1, y, game_board): game_board[x-1][y] = negate(game_board[x-1][y])
    if checkValid(x+1, y, game_board): game_board[x+1][y] = negate(game_board[x+1][y])
    return game_board




blueconnect.wait_for_connect()
play4 = False

#Starting game'
matrix.print_message("Starting game")

if(play4):
    c, r = 4, 4
else:
    c, r = 8, 8

game_board = [[0 for x in range(c)] for y in range(r)]

#Randomize Game board
for times in range(0, 30):
    game_board = randomize(game_board)
    printToBoard(game_board, play4)
    time.sleep(0.05)

#Wait for play move
while hasWon(game_board) == False:
    input = blueconnect.getNext()
    inputArray = input.split(",")
    print(inputArray)
    x = int(inputArray[1])
    y = int(inputArray[0])
    game_board = move(x, y, game_board)
    printToBoard(game_board, play4)

for i in range(11):
    matrix.invert(i%2)
    time.sleep(0.2)

matrix.print_message("Winner")