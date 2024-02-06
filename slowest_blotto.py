# note to self: using treehacks env
import csv
import itertools
import json

def sums(length, total_sum):
    if length == 1:
        yield (total_sum,)
    else:
        for value in range(total_sum + 1):
            for permutation in sums(length - 1, total_sum - value):
                yield (value,) + permutation

def game(player1, player2, numCastles):
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
    
def tournament(numTroops, numCastles):
    strategies = list(sums(numCastles, numTroops))
    competitors = {}
    for allocation in strategies:
        competitors[allocation] = [0, 0, 0]
    file_data = []
    highest_score = 0
    gameMatrix = [[0 for i in range(len(strategies))] for j in range(len(strategies))]
    for i, player1 in enumerate(competitors):
        for j, player2 in enumerate(competitors):
            result = game(player1, player2, numCastles)
            gameMatrix[i][j] = result
            if result == 1:
                competitors[player1][0] += 1
                competitors[player2][1] += 1
            if result == -1:
                competitors[player2][0] += 1
                competitors[player1][1] += 1
            else:
                competitors[player1][2] += 1
                competitors[player2][2] += 1
    file_data.append(str(competitors))
    file_data.append(str(gameMatrix))
    filename = f"C{numCastles:02}-T{numTroops:03}.txt"

    with open(filename, "w") as fle:
        json.dump(file_data, fle)

def csvtournament(numTroops, numCastles):
    strategies = list(sums(numCastles, numTroops))
    competitors = {}
    for allocation in strategies:
        competitors[allocation] = [0, 0, 0]
    winners = []
    highest_score = 0
    gameMatrix = [[0 for i in range(len(strategies))] for j in range(len(strategies))] 
    for i, player1 in enumerate(competitors):
        for j, player2 in enumerate(competitors):
            result = game(player1, player2, numCastles)
            gameMatrix[i][j] = result
            if result == 1:
                competitors[player1][0] += 1 # Player 1 win
                competitors[player2][1] += 1 # Player 2 loss
            if result == -1:
                competitors[player2][0] += 1 # Player 2 win
                competitors[player1][1] += 1 # Player 1 loss
            if result == 0:
                competitors[player1][2] += 1 # tie
                competitors[player1][2] += 1 # tie
    all_scores = competitors.values()
    highest_score = max(all_scores)
    for player in competitors:
        if competitors[player] == highest_score:
            winners.append(player)
    print(gameMatrix)

    fields = ["win_percentile"]
    for i in range(1, numCastles + 1):
        fields.append("c" + str(i))
    rows = []
    for strategy in competitors:
        profile = [(competitors[strategy][0]/competitors[strategy][0] + competitors[strategy][1] + competitors[strategy][2])]
        for troops in strategy:
            profile.append(troops)
        rows.append(profile)
    filename = 'csvBlotto, numCastles = ' + str(numCastles) + ", numTroops =" + str(numTroops)
    # writing to csv file
    with open(filename, 'w') as csvfile:
    # creating a csv writer object
        csvwriter = csv.writer(csvfile)

    # writing the fields
        csvwriter.writerow(fields)

    # writing the data rows
        csvwriter.writerows(rows)

tournament(2,100)