#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Dec  3 09:36:35 2022

@author: u0107886
"""

file1 = open('AOCD3.txt', 'r')
Lines = file1.read().splitlines()
#print(Lines)    
commontypes = []

for line in Lines:
    print(line)
    commontypes1bag = []
    half = int(len(line)/2)
    #print(half)
    #print(len(line))
    firstpart = line[:half]
    secondpart = line[half:]
    
    for type in firstpart:    
        if type in secondpart:
            commontypes1bag.append(type)
    print(commontypes1bag)
    uniquetype = set(commontypes1bag)
    print(uniquetype)
    commontypes.append(uniquetype)

print(commontypes)
"""
#calculate the priority score
#going to try this through the index, less hardcoding of numbers
priority_scores = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]
upper_priority_scores = []
for score in priority_scores:
    upper_score = score.upper()
    upper_priority_scores.append(upper_score)
priority = priority_scores + upper_priority_scores
#print(priority)

#define index of the commontypes, the index is the point so add that to the score
priorityscores = 0
#back to a list
for type in commontypes:
    for element in type:
        print(element)
        score = priority.index(element)
    #print(priority.index("A"))
    #print(score)
        priorityscores += score +1
print(priorityscores)
    
"""