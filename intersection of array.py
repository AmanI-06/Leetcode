def intersection(a,b):
    l=[]
    for i in a:
        if i in b:
            l.append(i)
    return l

if __name__=="__main__":
    aa=list(map(int,input().split(',')))
    bb=list(map(int,input().split(',')))
    print(intersection(aa,bb))

    