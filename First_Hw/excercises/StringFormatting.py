def print_formatted(number):
    L=len(bin(number))-2
    for i in range(1,number+1):
        l=len(bin(i))-2
        print((L-len(str(i)))*" ",i,(L+3-len(oct(i)))*" ",oct(i)[2:],(L+3-len(hex(i)))*" ",hex(i)[2:].upper(),sep="",end=(L-l+1)*" ")
        print(bin(i)[2:],end="\n")

