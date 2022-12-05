#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Dec  5 09:48:15 2022

@author: u0107886
"""
#create an empty array
import numpy as np
boxes = np.empty([3, 3], str)
emptyboxesontop = np.empty([3, 3], str)
#print(boxes)
#print(emptyboxesontop)
boxes[boxes == ""] = " "
emptyboxesontop[emptyboxesontop == ""] = " "

file1 = open('AOCD5b.txt', 'r')
boxes_commands = file1.read().splitlines()

#append boxes to array

for i in range(3):

    boxes[i, 0] = boxes_commands[i][1]     
    boxes[i, 1] = boxes_commands[i][5]
    boxes[i, 2] = boxes_commands[i][9]
boxes = np.concatenate((emptyboxesontop, boxes), axis=0)




#take the commands and iterate over the commands, parsing the info
commands = []
i = 5
commands = boxes_commands[5:]
for command in commands:
    print(command)
    listcommand = command.split(" ")
    num_boxes = int(listcommand[1])
    #print(num_boxes)
    startloc = int(listcommand[3])
    #print(startloc)
    endloc = int(listcommand[-1])
    #print(endloc)

    #now use this info to manipulate the array
    #iterate this command depending on the num_boxes
    while num_boxes > 0:
        print("still running the command")
        num_boxes -= 1
        #whilst iterating find the top box for the startloc
        #how to find the top of the box?
        for box in boxes:
            print(box)
            if box[startloc - 1] != " ":
                print("found the top box, we stop looking")
                selected_box = box[startloc - 1]
                #delete the box in that location
                box[startloc - 1] = " "
                #add that box to the top of the endloc
                break
        
        #implement that value in another location
        #on this level we are still within a command, we have the selected_box
        #find where it can be put in the array, it is the last location with an empty space
        #find the first location with empty space [x,y]
        #the space above it is [x-1, y] with y beind endloc and x-1 the previous boxline
        box_line = -1
        for box in boxes: #this loops 3 times because we have 3 box lines
            #print(boxes)
            if box[endloc - 1] != " ":
                #print(box_line)
                box_line += 1
                print("we can calculate the location of the storage")
                #print(box_line)
                boxes[box_line, endloc-1] = selected_box
                
                
                
                break
            
        print("command done")
        print(boxes)
    print("all boxes in this command are moved")

    print(boxes)
