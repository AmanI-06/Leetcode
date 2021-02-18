""" from collections import defaultdict
def common(A,B,C):
    map=collections.defaultdict(int)
    out=[]
    for num in A:
        map[num]+=1
    for num in B:
        map[num]+=1
    for num in C:
        map[num]+=1
    for key,value in map.items():
        if value==3:
            out.append(key)
    return out
 """
def common(a,b,c):
    one=0
    two=0
    three=0
    out=[]
    while one<len(a) and two<len(b) and three< len(c):
        if a[one] ==b[two] ==c[three]:
            out.append(a[one])
            one+=1
            two+=1
            three+=1
        elif b[two] < a[one]:
            two+=1
        elif c[three] <a[one]:
            three+=1
        else:
            one+=1
    return out
a=[1,2,3,4,5]
b=[3,4,5,6,7,8,9]
c=[1,2,5,6,]
print(common(a,b,c))