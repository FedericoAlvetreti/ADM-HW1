def minion_game(string):
    vocali=["A","E","I","O","U"]
    Stuart=[]
    Kevin=[]
    Pk=0
    Ps=0

    for i in range(0,len(string)):
        t=len(string)-i
        if string[i] in vocali:
            Pk+=t
        else:
            Ps+=t
    if Pk>Ps:
        print("Kevin "+str(Pk))
    elif Pk==Ps:
        print("Draw")
    else:
        print("Stuart "+str(Ps))
