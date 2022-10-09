n=int(input())
for i in range(n):
    k=input().split()
    try:
        print(int(k[0])//int(k[1]))
        
    except ZeroDivisionError as e:
        print("Error Code:",e)
    except ValueError as e:
        print("Error Code:",e)
