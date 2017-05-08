__author__ = 'Curti_000'

import BoardConfig as b
import Game as Game

def solveBacktracking(board, game4):
    config = b.BoardConfig(board, None)
    quin = backtrack(config, game4)
    return quin

def backtrack(config, game4):
    # print("Current config:",config)
    if(config.isGoal()):
        Game.printToBoard(config.board, game4)
        # print("Goal config:",config)
        return config
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
                  ,m   ,m pass
        return []

