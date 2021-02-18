def maxsum(a,n): #o(n)
    gs=a[0]
    ls=0
    st=0
    end=0
    poi=0
    for i in range(0,n):
        ls=ls+a[i]
        if(gs<ls):
            gs=ls
            st=poi
            en=i
        if(ls<0):
            ls=0
            poi=poi+1
    return gs

if __name__=='__main__':
    nn=int(input())
    aa=list(map(int,input().split(' ')))
    f=maxsum(aa,nn)
    print(f)