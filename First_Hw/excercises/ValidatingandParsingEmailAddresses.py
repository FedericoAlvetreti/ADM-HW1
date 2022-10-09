import re
for i in range(int(input())):
    line=input()
    match=re.search(r"<[a-zA-Z][\w\.\_\-]+@[a-zA-Z]+\.[a-zA-Z]{1,3}>",line)
    if match:
        print(line)
        
