# Enter your code here. Read input from STDIN. Print output to STDOUT
x=int(input())

for i in range(x):
     print(("H"*i).rjust(x-1)+"H"+("H"*i).ljust(x))
for i in range(x+1):
    print(("H"*x).center(2*x)+(" "*x).center(2*x)+("H"*x).center(2*x))
for i in range((x+1)//2):
    print(("H"*5*x).center(6*x))
for i in range(x+1):
    print(("H"*x).center(2*x)+(" "*x).center(2*x)+("H"*x).center(2*x))
for i in range(x-1,-1,-1):
    print((" ").center(4*x)+("H"*i).rjust(x-1)+"H"+("H"*i).ljust(x))
    
