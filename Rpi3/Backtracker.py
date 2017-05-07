__author__ = 'Curti_000'

import Rpi3.BoardConfig as b
import Rpi3.Game as Game

def solveBacktracking(board, game4):
    config = b.BoardConfig(board, None)
    return backtrack(config, game4)

def backtrack(config, game4):
    if(config.isGoal):
        Game.printToBoard(config.board, game4)
        return config
    else:
        for child in config.getSuccessors():
            if(child.isValid()):
                Game.printToBoard(config.board, game4)
                sol = solveBacktracking(child)
                if(len(sol) == 1):
                    return sol
            else:
                pass
        return []

