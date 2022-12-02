#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Dec  2 12:47:22 2022

@author: u0107886
"""

file1 = open('AOCD2.txt', 'r')
Lines = file1.read().splitlines()
print(Lines)
score = 0
for line in Lines:
    line = line.split()
    print(line[0])
    print(line[1])
    if line[0] == "A":
        if line[1] == "X":
            #print("need to lose")
            score += 3
        if line[1] == "Y":
            #print("need to draw")
            score += 4
        if line[1] == "Z":
            #print("need to win")
            score += 8
    if line[0] == "B":
        if line[1] == "X":
            #print("need to lose")
            score += 1 
        if line[1] == "Y":
            #print("need to draw")
            score += 5
        if line[1] == "Z":
            #print("need to win")
            score += 9
    if line[0] == "C":
        if line[1] == "X":
            #print("need to lose")
            score += 2
        if line[1] == "Y":
            #print("need to draw")
            score += 6
        if line[1] == "Z":
            #print("need to win")
            score += 7
print(score)
            