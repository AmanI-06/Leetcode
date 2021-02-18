def findDuplicate(l):
   for i in range(0,len(l)-1):
        if l.count(l[i])>1:
            return l[i]
       
l1=[1,2,5,5,6]
print(findDuplicate(l1))