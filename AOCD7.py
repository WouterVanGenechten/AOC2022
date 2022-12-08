#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Dec  7 08:15:28 2022

@author: u0107886
"""

file1 = open('AOCD7a.txt', 'r')
terminal = file1.read().splitlines()
directories = []
countlevel = 0
i = 0
for line in terminal:
    splitline = line.split(" ")
    #print(splitline)
    if len(splitline) == 3 and splitline[-1] != "..":
        i = terminal.index(line)        
        #print("found a directory")
        #print(splitline[-1])
        directory_entry = [splitline[-1]]        
        directories.append(directory_entry)

    #append to the directory the elements of the list:
        for line in terminal[i+2:]:
            splitline = line.split(" ")
            if len(splitline) == 2 and splitline[-1] != "ls":
                
                directories[countlevel].append(list(splitline))
            else:
                countlevel += 1
                break

#now count the size of items within a directory
#am I going to put this in a dictionary?
directory_entries = {}
directory_sizes = {}


for directory in directories:    
    directory_entries[directory[0]] = directory[1:]
#I need to build this empty directory_sizes
#it is the same as directory entries, but empty
for directory in directories:
    directory_sizes[directory[0]] = 0



for directory in directory_entries:
    #print(directory)
    #print(directory_entries[directory])
    for item in directory_entries[directory]:
        #print(item)           
        if item[0] == "dir":
            #print("I need to retrieve the value deeper")
                #so here I need to recall this function??
                #here I need to enter the dictionary_entries using the item as a key
            #print(directory_entries[item[-1]])

            for item in directory_entries[item[-1]]:
                if item[0] == "dir":
                    for item in directory_entries[item[-1]]:
                        if item[0] == "dir":
                            for item in directory_entries[item[-1]]:
                                if item[0] == "dir":
                                    for item in directory_entries[item[-1]]:
                                        if item[0] == "dir":
                                            for item in directory_entries[item[-1]]:
                                                if item[0] == "dir":
                                                    for item in directory_entries[item[-1]]:
                                                        if item[0] == "dir":
                                                            for item in directory_entries[item[-1]]:
                                                                if item[0] == "dir":
                                                                    for item in directory_entries[item[-1]]:
                                                                        if item[0] == "dir":     
                                                                            for item in directory_entries[item[-1]]:
                                                                                if item[0] == "dir":
                                                                                    for item in directory_entries[item[-1]]:
                                                                                        if item[0] == "dir":
                                                                                            for item in directory_entries[item[-1]]:
                                                                                                if item[0] == "dir":
                                                                                                    for item in directory_entries[item[-1]]:
                                                                                                        if item[0] == "dir":
                                                                                                            print("reached 8 levels deep")
                                                                                                        else:
                                                                                                            directory_sizes[directory] += int(item[0])
                                                                                                else:
                                                                                                    directory_sizes[directory] += int(item[0])
                                                                                        else:
                                                                                            directory_sizes[directory] += int(item[0])
                                                                                else:
                                                                                    directory_sizes[directory] += int(item[0])
                                                                        else:
                                                                            directory_sizes[directory] += int(item[0])
                                                                else:
                                                                    directory_sizes[directory] += int(item[0])        
                                                        else:
                                                            directory_sizes[directory] += int(item[0])                                                            
                                                else:
                                                    directory_sizes[directory] += int(item[0])      
                                        else:
                                            directory_sizes[directory] += int(item[0])    
                                else:
                                    directory_sizes[directory] += int(item[0])
                        else:
                            directory_sizes[directory] += int(item[0])                                                            
                else:
                    directory_sizes[directory] += int(item[0])
                
                
            

            #iterate over this directory and retrieve number
            #print(directory_entries[value])
            #print(directory_entries[value])
        else:
            #print(value[0])
            directory_sizes[directory] += int(item[0])
print(directory_sizes)
              
