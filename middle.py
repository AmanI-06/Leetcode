def middle(A,B,C):
    g=max(A,B,C)
    h=min(A,B,C)
    if A !=g and A!=h :
        return A
    elif B!=g and B!=h :
        return B
    elif C!=g and C!=h:
        return C

if __name__=="__main__":
    a=int(input())
    b=int(input())
    c=int(input())
    z=middle(a,b,c)
    print(z)