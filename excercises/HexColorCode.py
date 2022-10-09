import re
k=int(input())
i=0
line=input()
while i<k-1:
    if "{" in line:
        i+=1
        line=input()
        while not("}" in line):
            match=re.findall(r"#[a-fA-F0-9]{3,6}",line)
            if match:
                for j in match:
                    print(j)
            line=input()
            i+=1
    else:
        line=input()  
        i+=1
        continue
