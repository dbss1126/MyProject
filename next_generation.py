# -*- coding: utf-8 -*-
import random
__author__ = 'dbss1126'
g=input("세대:")
gg=1
while gg <= 4:
    deck_1 = [7,38,1,24,31,7,7,2] #교배할 개체 1
    deck_2 = [7,24,46,1,24,2,7,33] #교배할 개체 2
    next = [0,0,0,0,0,0,0,0]
    a=0
    temp = 0
    while a != 4:
        temp = random.choice(deck_1)
        next[a]=temp
        deck_1.remove(temp)
        a = a+1
    while a != 8:
        temp = random.choice(deck_2)
        next[a]=temp
        deck_2.remove(temp)
        a = a+1
    record = open("%d-%d.txt"%(g,gg),'w')
    for i in next:
        record.write("%d\n"%i)
        record.flush()
    gg+=1
