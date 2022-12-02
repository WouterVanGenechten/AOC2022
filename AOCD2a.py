#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Dec  2 12:38:47 2022

@author: u0107886
"""
scores_p1 = {"A X":4, "A Y":8, "B X":1, "A Z":3, "C X":7, "B Y":5, "B Z":9, "C Y":2, "C Z":6}
score = 0
file1 = open('AOCD2.txt', 'r')
Lines = file1.read().splitlines()
print(Lines)
for line in Lines:
    #print(line)
    if line == "A X":
        #print("draw")
        score += 4
    if line == "B Y":
        #print("draw")
        score += 5
    if line == "C Z":
        #print("draw")
        score += 6
    if line == "A Y":
        score += 8
    if line == "A Z":
        score += 3
    if line == "B X":
        score += 1
    if line == "B Z":
        score += 9
    if line == "C X":
        score += 7
    if line == "C Y":
        score += 2
        
print(score)
        


