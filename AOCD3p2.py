#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Dec  3 11:21:25 2022

@author: u0107886
"""

file1 = open('AOCD3.txt', 'r')
Lines = file1.read().splitlines()
#print(Lines)
length = len(Lines)
grouped_elves = [[]] * 100
#print(grouped_elves)

count = 0
groupbadges = []
for i in range(int(len(Lines)/3)):
    print(Lines[0])
    grouped_elves[count] = Lines[:3]
    #print(grouped_elves[count])
    del Lines[:3]
    print(Lines)
    count += 1
    #print(count)

for group in grouped_elves:
    groupbag = []
    for type in group[0]:
        if type in group[1] and type in group[2]:
            #print(type)
            groupbag.append(type)
    #print(groupbag)
    uniquetype = set(groupbag)
    #print(uniquetype)
    groupbadges.append(uniquetype)
print(groupbadges)
#calculate the scores
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
for type in groupbadges:
    for element in type:
        print(element)
        score = priority.index(element)
    #print(priority.index("A"))
    #print(score)
        priorityscores += score +1
print(priorityscores)
