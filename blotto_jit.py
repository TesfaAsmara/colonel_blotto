import os
import json
from joblib import Parallel, delayed
from numba import jit
import itertools
import argparse

def sums(length, total_sum):
    if length == 1:
        yield (total_sum,)
    else:
        for value in range(total_sum + 1):
            for permutation in sums(length - 1, total_sum - value):
                yield (value,) + permutation

@jit
def game_jit(player1, player2, numCastles):
    '''
    returns  1 if 
             0 if 
            -1 if
            
    Inputs
        player1:
        player2:
        numCastles: 

    Variables
        p1_score: ...
        ...
        
    '''
    p1_score = 0
    p2_score = 0
    n = 0
    p1_wbt = 0
    p2_wbt = 0

    while p1_wbt < 3 and p2_wbt < 3 and n < numCastles:
        if player1[n] > player2[n]:
            p1_score += n + 1
            p1_wbt += 1
            p2_wbt = 0
        if player1[n] < player2[n]:
            p2_score += n + 1
            p2_wbt += 1
            p1_wbt = 0
        if player1[n] == player2[n]:
            p1_wbt = 0
            p2_wbt = 0
        n += 1

    while p1_wbt == 3 and n < numCastles:
        p1_score += n + 1
        n += 1
    while p2_wbt == 3 and n < numCastles:
        p2_score += n + 1
        n += 1

    if p1_score > p2_score:
        return 1
    if p1_score < p2_score:
        return -1
    if p1_score == p2_score:
        return 0

def play_game(i, j, player1, player2, numCastles, numTroops):
    result = game_jit(player1, player2, numCastles)

    filename = f"results/C{numCastles:02}_T{numTroops:03}/{i}_{j}_{result}.txt"

    file =  open(filename, "w")
    file.close()
    return

def tournament(numCastles, numTroops):
    strategies = list(sums(numCastles, numTroops))
    foldername = f"results/C{numCastles:02}_T{numTroops:03}"
    
    # create folder if doesn't exist
    if not os.path.exists(foldername):
        os.makedirs(foldername)
    
    results = Parallel(n_jobs=8)(
    delayed(play_game)(i, j, player1, player2, numCastles, numTroops) 
    for i, player1 in enumerate(strategies) 
    for j, player2 in enumerate(strategies) if i != j
    )
    return

def main():
    # Initialize parser
    parser = argparse.ArgumentParser(description='Play a series of games and record the results, sped up by jit.')
    
    # arguments for numCastles, numTroops
    parser.add_argument("-c", "--castles", required=True, type=int, help="Number of Castles")
    parser.add_argument("-t", "--troops", required=True, type=int, help="Number of Troops")
    
    # Read arguments from command line
    args = parser.parse_args()
    
    # Parameters
    numCastles = args.castles
    numTroops = args.troops
    
    # Run the tournament
    tournament(numCastles, numTroops)

if __name__ == "__main__":
    main()