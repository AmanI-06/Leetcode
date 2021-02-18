def kth(a,k):
    a.sort()
    f=len(a)
    for i in range(1,f+1):
        if i==(k):
            l=a[i-1]
    return l
    
if __name__=='__main__':
    aa=list(map(int,input().split(' ')))
    kk=int(input())
    g=kth(aa,kk)
    print(g)


