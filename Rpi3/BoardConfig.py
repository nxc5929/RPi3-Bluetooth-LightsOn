__author__ = 'Curti_000'

import Backtracker as bt

class BoardConfig:

    def __init__(self,board,boardconfig):
        if(boardconfig == None):
            self.isFirst = False
            self.dim = len(board)
            self.board = [[1 for x in range(self.dim)] for y in range(self.dim)]

            for row in range(self.dim):
                for col in range(self.dim):
                    self.board[row][col] = board[row][col]

            self.offInCol = [0 for col in range(self.dim)]
            self.offInRow = [0 for row in range(self.dim)]
            self.cursor = (0,0)

            for row in range(self.dim):
                for col in range(self.dim):
                    if board[row][col] == 0:
                        self.offInRow[row] += 1
                        self.offInCol[col] += 1
        else:
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

            if not self.isFirst:
                self.cursor = self.advanceCoord(boardconfig.cursor, self.dim)
            else:
                self.cursor = (boardconfig.cursor[0], boardconfig.cursor[1])
                self.isFirst = False

    def getSuccessors(self):
        successors = []

        if self.cursor[0] == self.dim - 1 and self.cursor[1] == self.dim - 1:
            return successors

        noTileClicked = BoardConfig(None, self)
        tileClicked = BoardConfig(None, self)

        tileClicked.activateCursorTile()

        successors.append(noTileClicked)
        successors.append(tileClicked)

        return successors

    def isValid(self):
        curRow = self.cursor[0]
        curCol = self.cursor[1]

        output = True

        for row in range(curRow - 1):
            if(self.offInRow[row] != 0):
                output = False

        return output

    def isGoal(self):
        output = True

        for rowValue in self.offInRow:
            if(rowValue != 0):
                output = False

        return output

    def advanceCoord(self, initial, dim):

        if initial[1] < self.dim - 1:
            x = initial[0]
            y = initial[1] + 1
        elif initial[1] == self.dim - 1 and initial[0] < dim - 1:
            x = initial[0] + 1
            y = 0
        else:
            print("Coordinate advanced too far in backtracking (BoardConfig):",initial)
            return None
        return x,y

    def activateCursorTile(self):
        self.activateTile(self.cursor)

    def activateTile(self, coord):
        row = coord[0]
        col = coord[1]

        self.swapState(self.board, row, col)

        if row - 1 >= 0:
            self.swapState(self.board, row - 1, col);

        if row + 1 < self.dim:
            self.swapState(self.board, row + 1, col);

        if col - 1 >= 0:
            self.swapState(self.board, row, col - 1);

        if col + 1 < self.dim:
            self.swapState(self.board, row, col + 1);

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
    board = [[0,0,1,0],[1,0,0,1],[0,0,1,0],[0,0,1,1]]

    # board[0][0] = 0
    #  board[0][1] = 0
    # board[0][2] = 1
    # board[0][3] = 0

    # board[1][0] = 1
    # board[1][1] = 0
    # board[1][2] = 0
    # board[1][3] = 1

    # board[2][0] = 0
    # board[2][1] = 0
    # board[2][2] = 1
    # board[2][3] = 0

    # board[3][0] = 0
    # board[3][1] = 0
    # board[3][2] = 1
    # board[3][3] = 1

    config = BoardConfig(board, None)
    print(bt.solveBacktracking(board, None))



