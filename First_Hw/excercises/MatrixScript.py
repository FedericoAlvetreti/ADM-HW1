#!/bin/python3

import math
import os
import random
import re
import sys




first_multiple_input = input().rstrip().split()

n = int(first_multiple_input[0])

m = int(first_multiple_input[1])

matrix=[]
line=[]
for i in range(n):
    matrix+=[list(input())]

for i in range(m):
    for j in range(n):
        line+=matrix[j][i]
line="".join(line)
print(re.sub(r"(?<=\w)\W+(?=\w)"," ",line))
