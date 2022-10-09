import re
n=int(input())
for i in range(n):
    line=input()
    line=(re.sub(r"(?<=\s)(&&)(?=\s)",r"and",line))
    line=(re.sub(r"(?<=\s)\|\|(?=\s)",r"or",line))
    print(line)
    
