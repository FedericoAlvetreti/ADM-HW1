import re
word,pat=input(),input()
k=0
while True:
    match=re.search(pat,word)
    if match:
        word=word[match.start()+1:]
        print((match.start()+k,match.end()-1+k))
        k+=match.start()+1
    else:
        break
if k==0:
    print((-1,-1))
    
