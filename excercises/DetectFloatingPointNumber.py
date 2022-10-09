import re
from collections import Counter

n=int(input())
for i in range(n):
    k=input()
    if (not(Counter(k)["."]==1)) :
        print(False)
    else:
        try:
            k=float(k)
            print(True)
        except ValueError:
            print(False)
    

            
