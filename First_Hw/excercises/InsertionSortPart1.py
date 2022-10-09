#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'insertionSort1' function below.
#
# The function accepts following parameters:
#  1. INTEGER n
#  2. INTEGER_ARRAY arr
#

def insertionSort1(n, arr):
    for i in range(n-1,0,-1):
        if arr[i]<arr[i-1]:
            for j in arr:
                if j==arr[i]:
                    print(arr[i-1],end=" ")
                else:
                    print(j,end=" ")
            print("")
            k=arr[i]
            arr[i]=arr[i-1]
            arr[i-1]=k
        else:
            break
    for j in arr:
        print(j,end=" ")
    return()
if __name__ == '__main__':
    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    insertionSort1(n, arr)
