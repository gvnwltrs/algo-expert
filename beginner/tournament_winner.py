#!/usr/bin/env python3

def tournamentWinner(competitions, results):
    winners = []
    final_winner = ""
    
    for i in range(len(competitions)):
        if results[i]:
            winners.append(competitions[i][0])
        else:
            winners.append(competitions[i][1])

    print(winners)
    final_winner = max(set(winners), key = winners.count)

    return final_winner