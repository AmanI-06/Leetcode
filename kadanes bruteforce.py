def bru(a,n):   #o(n^2)
    maxs=0
    s=0
    for i in range(0,len(a)):
        for j in range(i,len(a)):
            s=s+a[j]
            if(s>maxs):
                maxs=s
        s=0    
    return maxs
        
if __name__=="__main__":
    nn=int(input())
    aa=list(map(int,input().split(' ')))
    f=bru(aa,nn)
    print(f)
