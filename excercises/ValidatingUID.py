import re
from collections import Counter

for i in range(int(input())):
    line=input().strip()
    if not re.search(r"[a-zA-Z0-9]{10}",line) or len(Counter(line))!=10:
        print("Invalid")
    else:
        dig=0
        up=0
        low=0
        for j in line:
            if j.isupper():
                up+=1
            elif j.isdigit():
                dig+=1
        if up>=2 and dig>=3:
            print("Valid")
        else:
            print("Invalid")
            
