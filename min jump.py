def jump(n,arr):
    c=n
    count=0
    s=arr[0]
    for i in range(0,n+1,s):
        if c>=0:
            c=c-arr[i]
            count+=1
            print(c)
        s=arr[i]
        print(s)

    #print(count)   
    

m=9
a=[5,6,2,1,3,1,3,6,7]
jump(m,a)