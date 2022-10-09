#!/bin/python3

import math
import os
import random
import re
import sys
from collections import Counter

if __name__ == '__main__':
    s = input()
    s=Counter(s)
    lista=[]
    for i in s:
        lista+=[(i,s[i])]
    lista=sorted(lista,key=lambda t:t[1], reverse=True)
    for i in range(len(lista)):
        listai=[]
        for j in range(i,len(lista)):
            if lista[i][1]==lista[j][1]:
                listai+=[lista[j]]
            elif lista[i][1]>lista[j][1]:
                break
        listai=sorted(listai,key=lambda t:t[0])
        lista[i:j]=listai
    for i in range(3):
        print(lista[i][0],lista[i][1],sep=" ")
