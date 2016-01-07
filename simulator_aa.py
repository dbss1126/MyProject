#-*- coding: cp949 -*-
__author__ = 'dbss1126'
import random
gene = [0,1,2]
random_pick=[0,1]
num_1 = input("개체수:")
repeat = input("반복:")
num = num_1
first = range(1,num+1,1)
while num != 0:
    first[num-1] = random.choice(gene)
    num = num-1
num = num_1
a = num
b = num
c = num
n_0 = 0
n_1 = 0
n_2 = 0
temp = 0
t1=0
first_s1 = long(range(1,a+1,1))
first_s2 = long(range(1,b+1,1))
second = long(range(1,c+1,1))
#print(first)
print("0:"+str(first.count(0)),"1:"+str(first.count(1)),"2:"+str(first.count(2)))
print("0:"+(str(first.count(0)*2+(first.count(1)))),"1:"+(str(first.count(2)*2+(first.count(1)))))
while repeat != 0:
    num = num_1
    a = num
    b = num
    c = num
    temp = 0
    while a != 0:
        temp =  random.choice(random_pick)
        t1 = random.choice(first) + random.choice(first)
        if t1 == 0:
            second[a-1] = 0
        elif t1 == 2:
            second[a-1] = 1
        elif t1 == 4:
            second[a-1] = 2
        elif t1 == 1:
            if temp == 0:
                second[a-1] = 0
            else:
                second[a-1] = 1
        elif t1 == 3:
            if temp == 0:
                second[a-1] = 1
            else:
                second[a-1] = 2
        a = a-1
    #print(second)
    print("0:"+(str(second.count(0)*2+(second.count(1)))),"1:"+(str(second.count(2)*2+(second.count(1)))))
    first = second
    repeat = repeat-1

