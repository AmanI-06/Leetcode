import math
def med(v,x):
    a=[]
    a=v+x
    a.sort()
    print(a)
    if len(a)%2!=0:
        x=math.floor(len(a)/2)
        return a[x]
    else:
        x=len(a)//2
        return (a[x-1]+a[x])//2

z=[4,6,2,3,9,7]
b=[-13,-12,-9]
print(med(z,b))