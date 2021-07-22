def replaceElements(arr):
            for i in range(0,len(arr)):
                if i<len(arr)-1:
                    arr[i]=max(arr[i+1:])
                else:
                    arr[i]=-1
            return arr 
print(replaceElements([17,18,5,4,6,1]))
