def rev(a):
    for i in range(len(a)-1,-1,-1):
        print(a[i],end=' ')
    return

if __name__=='__main__':
    f=list(input().split(' '))
    rev(f)
    

