def rotate( n,arr):
    l=[]
    l.append(arr[-1])
    for i in range(0,n-1):
        l.append(arr[i])
    return l
    
if __name__=='__main__':
    kk=int(input())
    aa=list(map(int,input().split(',')))
    g=rotate(kk,aa)
    print(*g)
    
""" def rotate(arr,n):  #this can also be used in the above function
    x = arr[n - 1] 
      
    for i in range(n - 1, 0, -1): 
        arr[i] = arr[i - 1]; 
          
    arr[0] = x;  """
  

