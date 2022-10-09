import re

for i in range(int(input())):
    line=input()
    if (re.fullmatch(r"[456]\d{15}|[456]\d{3}(\-\d{4}){3}", line) and \
         not re.search(r"([0-9])(\1){3}", line.replace("-",""))):
        print("Valid")
    else:
        print("Invalid")
        
        
        
        
        
