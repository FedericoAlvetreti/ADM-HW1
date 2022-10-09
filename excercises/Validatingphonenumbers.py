import re

def fun(line):
    try:
        line=int(line)
        return(True)
    except ValueError:
        return(False)
    
for i in range(int(input())):
    line=input()
    if re.match(r"[789]",line) and len(line)==10 and fun(line):
        print("YES")
    else:
        print("NO")
