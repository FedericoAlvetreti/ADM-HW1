#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'insertionSort2' function below.
#
# The function accepts following parameters:
#  1. INTEGER n
#  2. INTEGER_ARRAY arr
#

def insertionSort1(n,arr):
    for i in range(n-1,0,-1):
        if arr[i]<arr[i-1]:
            k=arr[i]
            arr[i]=arr[i-1]
            arr[i-1]=k
        else:
            break
    return(arr)



def insertionSort2(n, arr):
    for j in range(1,n):
        arr=insertionSort1(j+1,arr[0:j+1])+arr[j+1:]
        for i in arr:
            print(i,end=" ")
        print("")
        
if __name__ == '__main__':
    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    insertionSort2(n, arr)
