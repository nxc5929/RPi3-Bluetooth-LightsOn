__author__ = 'Curti_000'

import BoardConfig as b
import Game as Game

# solves a game board using backtracking
def solveBacktracking(board, game4):
    config = b.BoardConfig(board, None)
    final = backtrack(config, game4)
    return final

# a helper method for solveBacktracking
def backtrack(config, game4):
    # print("Current config:",config)

    # if we have our goal, print it and end recursion
    if(config.isGoal()):
        Game.printToBoard(config.board, game4)
        # print("Goal config:",config)
        return config
    # else, get successors, check if valid, display and recurse.
    else:
        for child in config.getSuccessors():
            if(child.isValid()):
                Game.printToBoard(config.board, game4)
                # print("\tValid successor:", config)
                sol = backtrack(child, game4)
                if(sol != []):
                    return sol
            else:
                #print("\tInvalid successor:", config)
                pass
        # no successors, no solution
        return []

