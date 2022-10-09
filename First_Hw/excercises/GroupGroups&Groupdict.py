import re
match=re.search(r"([1-9A-Za-z])\1+",input())
if match :
    print(match.group()[0]) 
else :
    print(-1)
