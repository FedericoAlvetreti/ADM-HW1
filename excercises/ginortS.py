word=input()
even=[]
odd=[]
lower=[]
upper=[]
for i in word:
    if i.isalpha():
        if i.isupper():
            upper+=i
        else:
            lower+=i
    else:
        if int(i)%2==0:
            even+=i
        else:
            odd+=i
even.sort()
odd.sort()
lower.sort()
upper.sort()
print("".join(lower)+"".join(upper)+"".join(odd)+"".join(even))
            
