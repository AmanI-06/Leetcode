def primepartition(m):
  arr=[True for i in range(m+1)]
  n=2
  b=[]
  s=0
  while(n*n<=m):
    if arr[n]==True:
        for i in range(n*n,m+1,n):
            arr[i]=False
    n=n+1
  for n in range(2,m+1):
    if arr[n]==True :
        b.append(n)
  print(b)
  for i in range(0,len(b)-1):
      for j in range(i,len(b)-1):
            s=b[i]+b[j]
            if (s==m):
                return True
  return False
        
        
    
print(primepartition(7))