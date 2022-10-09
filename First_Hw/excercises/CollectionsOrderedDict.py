n,items=int(input()),{}
for i in range(n):
    k=input()
    for j in range(len(k)):
        if k[j].isdecimal():
            k=(k[:j].strip(),k[j:].strip())
            break
    if k[0] in items:
        items[k[0]]+=int(k[1])
    else:
        items[k[0]]=int(k[1])
for i in items:
    print(i,items[i])   
