#!/usr/bin/env python3
# -*- coding: utf-8 -*-



file1 = open('AOCD4.txt', 'r')
pair_of_elves = file1.read().splitlines()
count = 0
countp2 = 0


#obviously splitting in pairs, then lots of stuff to split it and make the range
#of each elf
for pair in pair_of_elves: 
    firstrangeplaceholder = []
    #print(pair)
    splitpair = pair.split(",")
    firstelf = splitpair[0]
    secondelf = splitpair[1]
    firstelf = firstelf.split("-")  
    secondelf = secondelf.split("-")
    first = int(firstelf[0])
    second = int(firstelf[-1]) + 1    
    firstb = int(secondelf[0])
    secondb = int(secondelf[-1]) + 1 
    firstrange = list(range(first, second))
    if firstrange[0] == firstrange[-1]:
        #print("there is a double")
        firstrangeplaceholder.append(firstrange[0])
        firstrange = firstrangeplaceholder
    secondrange = list(range(firstb, secondb))
    #print(firstrange)
    #print(secondrange)
        
#data formatted
#now check whether the first elf is in the second elf
#if first fits in second AND second fits in first we would get a count too many
#therefore remove that count 
    #print(pair)
    testing_pair = pair
    if all(item in firstrange for item in secondrange):
        count+=1
    if all(item in secondrange for item in firstrange):
        count+=1
    if all(item in firstrange for item in secondrange) and all(item in secondrange for item in firstrange):
        count-=1


    for x in firstrange:
        #print(x)
        if x in secondrange:
            #print("in there, early break")
            countp2 += 1
            break
        else:
            #print("not in there")
            pass
print("answer for first part")
print(count)
print("the answer for part 2")            
print(countp2)
