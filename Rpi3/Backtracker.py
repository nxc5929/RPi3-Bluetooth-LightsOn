__author__ = 'Curti_000'

import BoardConfig as b
import Game as Game
#Starts the backtracker search
def solveBacktracking(board, game4):
    config = b.BoardConfig(board, None)
    quin = backtrack(config, game4)
    return quin

#current branch to seatch
def backtrack(config, game4):
    # print("Current config:",config)
    # see if the goal is meet
    if(config.isGoal()):
        #prints to board
        Game.printToBoard(config.board, game4)
        # print("Goal config:",config)
        return config
    else:
        #backtracks until valid board is found
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
        return []

