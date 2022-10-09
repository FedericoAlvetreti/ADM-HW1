

# Complete the solve function below.
def solve(s):
    s=list(s)
    if s[0]!=" ":
        s[0]=s[0].upper()
    for i in range(0,len(s)):
        if s[i-1]==" " and s[i]!=" ":
            s[i]=s[i].upper()
    s="".join(s)
    return(s)
