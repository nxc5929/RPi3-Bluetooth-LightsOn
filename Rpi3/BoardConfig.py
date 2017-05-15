__author__ = 'Curti_000'

import Backtracker as bt

# used to represent a specific board in backtracking
class BoardConfig:

    # creates a boardconfig.
    # If no previous boardconfig given, make an original one from a board.
    # If boardconfig given, acts as copy constructor, copying the state of the previous.
    def __init__(self,board,boardconfig):
        if(boardconfig == None):
            # whether this boardconfig is the first boardconfig,
            # in terms of a single chain of backtracking
            self.isFirst = False

            # dimensions of the board. Must be square
            self.dim = len(board)

            # the board, to be copied and filled in
            self.board = [[1 for x in range(self.dim)] for y in range(self.dim)]

            # copy the old board over to the new one
            for row in range(self.dim):
                for col in range(self.dim):
                    self.board[row][col] = board[row][col]

            # offInCol and offInRow are arrays if how many 0s are in each
            # col and row, respectively
            self.offInCol = [0 for col in range(self.dim)]
            self.offInRow = [0 for row in range(self.dim)]

            # the cursor that is the current targeted tile for
            # the derivation of successors
            self.cursor = (0,0)

            # initialize offInRow and offInCol to correct values
            for row in range(self.dim):
                for col in range(self.dim):
                    if board[row][col] == 0:
                        self.offInRow[row] += 1
                        self.offInCol[col] += 1
        else:
            # copy all values
            self.isFirst = boardconfig.isFirst
            self.dim = boardconfig.dim
            self.board = [[1 for x in range(self.dim)] for y in range(self.dim)]

            for row in range(self.dim):
                for col in range(self.dim):
                    self.board[row][col] = boardconfig.board[row][col]

            self.offInCol = [0 for col in range(self.dim)]
            self.offInRow = [0 for row in range(self.dim)]

            for row in range(len(self.offInRow)):
                self.offInRow[row] = boardconfig.offInRow[row]
            for col in range(len(self.offInCol)):
                self.offInCol[col] = boardconfig.offInCol[col]

            # only advance the coordinates of the cursor of the successors if
            # not the first boardconfig, which needs to fill in values for
            # the first tile with its successors
            if not self.isFirst:
                self.cursor = self.advanceCoord(boardconfig.cursor, self.dim)
            else:
                self.cursor = (boardconfig.cursor[0], boardconfig.cursor[1])
                self.isFirst = False

    # creates boards which represent the options for the
    # next move on the board. Generates a move and not moving on that tile
    def getSuccessors(self):
        successors = []

        # if not last tile
        if self.cursor[0] == self.dim - 1 and self.cursor[1] == self.dim - 1:
            return successors

        # the two options for next board moves
        noTileClicked = BoardConfig(None, self)
        tileClicked = BoardConfig(None, self)

        tileClicked.activateCursorTile()

        successors.append(noTileClicked)
        successors.append(tileClicked)

        return successors

    # returns whether a config is valid or not
    # this is based on the rules of the game
    def isValid(self):
        curRow = self.cursor[0]
        curCol = self.cursor[1]

        valid = True

        if(curRow > 1):
            for row in range(curRow - 2):
                if(self.offInRow[row] != 0):
                    valid = False
        if(curRow > 0 and curCol > 0):
            for col in range(curCol - 1):
                if(self.board[curRow - 1][col] == 0):
                    valid = False
        return valid

    # returns whether the config is the goal config,
    # where the game is won
    def isGoal(self):
        goal = True

        for rowValue in self.offInRow:
            if(rowValue != 0):
                goal = False

        return goal

    # return the next coordinates to check,
    # when given the initial position, and the size of the board
    def advanceCoord(self, initial, dim):

        # if not at end of row, move along row
        if initial[1] < self.dim - 1:
            x = initial[0]
            y = initial[1] + 1
        # if at end of row, but not last row
        elif initial[1] == self.dim - 1 and initial[0] < dim - 1:
            x = initial[0] + 1
            y = 0
        # if on last tile
        else:
            print("Coordinate advanced too far in backtracking (BoardConfig):",initial)
            return None

        return x,y

    # used to make a move on the current cursor tile
    def activateCursorTile(self):
        self.activateTile(self.cursor)

    # used to make a move on any tile in the board
    def activateTile(self, coord):
        row = coord[0]
        col = coord[1]

        # swaps the state of the selected tile
        self.swapState(self.board, row, col)

        # swap state of left adjacent tile, if exists
        if row - 1 >= 0:
            self.swapState(self.board, row - 1, col);

        # swap state of right adjacent tile, if exists
        if row + 1 < self.dim:
            self.swapState(self.board, row + 1, col);

        # swap state of above adjacent tile, if exists
        if col - 1 >= 0:
            self.swapState(self.board, row, col - 1);

        # swap state of below adjacent tile, if exists
        if col + 1 < self.dim:
            self.swapState(self.board, row, col + 1);

    # swaps the state of a tile on the board,
    # updating offInRow and offInCol
    def swapState(self, board, row, col):
        if board[row][col] == 0:
            board[row][col] = 1
            self.offInRow[row] = self.offInRow[row] - 1
            self.offInCol[col] = self.offInRow[col] - 1
        else:
            board[row][col] = 0
            self.offInRow[row] = self.offInRow[row] + 1
            self.offInCol[col] = self.offInRow[col] + 1

    def __str__(self):
        printer = self.cursor.__str__() + '\n'
        for row in range(self.dim):
            for col in range(self.dim):
                if self.cursor[0] == row and self.cursor[1] == col:
                    printer += "* "
                else:
                    printer += self.board[row][col].__str__() + " "
            printer += "\n"

        printer += self.offInRow.__str__() + "," + self.offInCol.__str__() + "\n";
        return printer

if __name__ == '__main__':
    board = [[1 for x in range(4)] for y in range(4)]

    board[0][0] = 0
    board[0][1] = 0
    board[0][2] = 1
    board[0][3] = 0

    board[1][0] = 1
    board[1][1] = 0
    board[1][2] = 0
    board[1][3] = 1

    board[2][0] = 0
    board[2][1] = 0
    board[2][2] = 1
    board[2][3] = 0

    board[3][0] = 0
    board[3][1] = 0
    board[3][2] = 1
    board[3][3] = 1

    config = BoardConfig(board, None)
    print(bt.solveBacktracking(board, None))



