# -*- coding: utf-8 -*-
__author__ = 'dbss1126'
import random
g=input("세대:")
##########함수 초기화##############
def reset():
    global card,card_temp,card_temp_str,ai_deck,ai_deck_text,ai_deck_str,a,set,temp,win,draw,lose,ai_sum
    card = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43,44,45,46,47,48,49,50,51,52]
    card_temp = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43,44,45,46,47,48,49,50,51,52]
    card_temp_str = []
    ai_deck = [0,0,0,0,0,0,0,0]
    ai_deck_text = [0,0,0,0,0,0,0,0]
    ai_deck_str = []
    a = 0
    set = 1
    temp = 0
    win = 0
    draw = 0
    lose = 0
    ai_sum = 0
##########함수 초기화##############

##########세대 제작###############
def generate():
    global gg
    global ggg
    ggg=0 #유전자 번호
    gg=1 #개체 번호
    while gg <= 4:
            record = open('%d-%d.txt'%(g,gg),'w')
            while ggg != 8:
                    record.write("%d\n"%random.choice(card_temp))
                    record.flush()
                    ggg+=1
            gg+=1
            ggg=0
    record.close()
    gg=1
    ggg=0
##########세대 제작###############

#############개체1 읽어오기###############
def read_1():
    g1=open('%d-1.txt'%g,'r')
    data = g1.readlines()
    global deck_1
    global deck_1_sum
    deck_1=[0,0,0,0,0,0,0,0]
    deck_read=0
    for i in data:
        deck_1[deck_read]=eval(i.strip())
        deck_read+=1
    print(deck_1)
    deck_1_sum=sum(deck_1, 0.0)
    g1.close()
    g2=open('%d-1.txt'%g,'a')
    g2.write("%d"%deck_1_sum)
    g2.close()
#############개체1 읽어오기###############

#############개체2 읽어오기###############
def read_2():
    g1=open('%d-2.txt'%g,'r')
    data = g1.readlines()
    global deck_2
    global deck_2_sum
    deck_2=[0,0,0,0,0,0,0,0]
    deck_read=0
    for i in data:
        deck_2[deck_read]=eval(i.strip())
        deck_read+=1
    print(deck_2)
    deck_2_sum=sum(deck_2, 0.0)
    g1.close()
    g2=open('%d-2.txt'%g,'a')
    g2.write("%d"%deck_2_sum)
    g2.close()
#############개체2 읽어오기###############

#############개체3 읽어오기###############
def read_3():
    g1=open('%d-3.txt'%g,'r')
    data = g1.readlines()
    global deck_3
    global deck_3_sum
    deck_3=[0,0,0,0,0,0,0,0]
    deck_read=0
    for i in data:
        deck_3[deck_read]=eval(i.strip())
        deck_read+=1
    print(deck_3)
    deck_3_sum=sum(deck_3, 0.0)
    g1.close()
    g2=open('%d-3.txt'%g,'a')
    g2.write("%d"%deck_3_sum)
    g2.close()
#############개체3 읽어오기###############

#############개체4 읽어오기###############
def read_4():
    g1=open('%d-4.txt'%g,'r')
    data = g1.readlines()
    global deck_4
    global deck_4_sum
    deck_4=[0,0,0,0,0,0,0,0]
    deck_read=0
    for i in data:
        deck_4[deck_read]=eval(i.strip())
        deck_read+=1
    print(deck_4)
    deck_4_sum=sum(deck_4, 0.0)
    g1.close()
    g2=open('%d-4.txt'%g,'a')
    g2.write("%d"%deck_4_sum)
    g2.close()
#############개체4 읽어오기###############

reset()
if g == 1:
    generate()
read_1()
read_2()
read_3()
read_4()
deck_sum = [0,0,0,0]
deck_sum[0]=deck_1_sum
deck_sum[1]=deck_2_sum
deck_sum[2]=deck_3_sum
deck_sum[3]=deck_4_sum

gggg=0
while gggg != 4:
    reset()
    print(deck_sum[gggg])
    record = open('result-%d.txt'%g,'a')
    record.write("개체%d총합:%d"%(gggg+1,deck_sum[gggg]))
    record.flush()
    while set < 100001:
        while a != 8:
            temp = random.choice(card_temp)
            ai_deck[a]=temp
            card_temp.remove(temp)
            a = a+1
        card_temp = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43,44,45,46,47,48,49,50,51,52]
        a = 0
        temp = 0
        ai_sum = sum(ai_deck, 0.0)
        ai_deck_str=[str(ai_deck)]
        if deck_sum[gggg] < ai_sum:
            print("승"+str(ai_deck))
            record.write("\n승")
            record.flush()
            record.writelines(ai_deck_str)
            record.flush()
            win = win + 1
        elif deck_sum[gggg] == ai_sum:
            print("무"+str(ai_deck))
            record.write("\n무")
            record.flush()
            record.writelines(ai_deck_str)
            record.flush()
            draw = draw + 1
        elif deck_sum[gggg] > ai_sum:
            print("패"+str(ai_deck))
            record.write("\n패")
            record.flush()
            record.writelines(ai_deck_str)
            record.flush()
            lose = lose + 1
        set = set + 1
    print("승:"+str(win))
    print("무:"+str(draw))
    print("패:"+str(lose))
    print(deck_sum[gggg])
    record.write("\n승:%d"%win)
    record.flush()
    record.write("\n무:%d"%draw)
    record.flush()
    record.write("\n패:%d\n"%lose)
    record.flush()
    g2=open("%d-%d.txt"%(g,gggg+1),'a')
    g2.write("\n승:%d"%win)
    g2.flush()
    g2.close()
    record.close()
    gggg+=1


