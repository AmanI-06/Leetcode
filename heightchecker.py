def heightChecker(hts):
    c=0
    h=sorted(hts)
    for i in range(len(hts)):
        if h[i]!=hts[i]:
            c+=1
    print(c)
heightChecker([5,6,7,1,1,1,0])