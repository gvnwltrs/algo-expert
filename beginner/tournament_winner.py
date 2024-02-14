#!/usr/bin/env python3

# Problem: 
# We're asked to imagine there is an algorithms tournament in which multiple 
# teams compete against each other. In each competition there will be two 
# teams that compete. There will be one winner and one loser out of all of 
# these competitions and there are no ties. Each team will compete against 
# all other teams exactly once. A team gets 3 points for each competition 
# it wins and 0 points for each competition it loses. It's guaranteed that 
# the tournament always has at least two teams and there will be only one 
# tournament winner. We are given two inputs, the competitions array and 
# the results array. We need to write a function that returns the winner of 
# the tournament, or more specifically, the name of the team that has the 
# most number of points. The competitions array is an array of pairs, 
# representing all of the competitions in the tournament. Inside of 
# these pairs, we have two strings: the first one is the name of the home 
# team and the second one is the name of the away team. The results array 
# represents the winner of each of these competitions. Inside the results 
# array, a 1 means that the home team won and a 0 means the away team won. 
# The results array is the same length as the competitions array, and the 
# indices in the results array correspond with the indices in the 
# competitions array.


def tournamentWinner(competitions, results):
    # home | away : 1 - home team won | 0 - away team won
    winners_for_each_round = [team[0]  if result == 1 else team[1] for team, result in zip(competitions, results)]
    winning_teams_to_count = set(winners_for_each_round)
    return max(winning_teams_to_count, key = winners_for_each_round.count)

# Time complexity: O(n) | Space complexity: O(k) - k is the number of teams

# Explanation:
'''
We use a list comprehension for a conditional to store each winning team. The zip 
portion of the comprehension allows us to iterate over two lists at the same time. 
If the result from the results lists is a 1 then we know the first index 0 of the 
teams list (home team) has won, so we store that. Else, we store the other team (away)
since we know that there are no ties and so the other team must have won.

We store the winning teams in a set to use as inputs to our max function 
used in the return. The set reduces any duplicates we have in our winning teams. 
The key portion is where we run our count() method on our winners list using the 
values we have from set as input (can think of this like using a map function). 
'''