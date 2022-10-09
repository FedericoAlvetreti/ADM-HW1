import re
word=input()
match=re.findall(r"[aeiouAEIOU][aeiouAEIOU]+",word)
for i in match:
    if not(re.search(r"\w"+i+"\w",word)):
        match.remove(i)
    else:
        print(i)
if match==[]:
    print(-1)
