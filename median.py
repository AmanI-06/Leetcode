import math
def med(v):
    a=[]
    v.sort()
    a=v
    print(a)
    if len(a)%2!=0:
        x=math.floor(len(a)/2)
        print(a[x])
    else:
        x=len(a)//2
        print (a[x-1]+a[x])//2

z=[4,6,2,3,9,7]
med(z)