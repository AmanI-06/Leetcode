def checkIfExist(arr):
    for i in range(len(arr)):
        for j in range(i+1,len(arr)):
            if((arr[j]==2*arr[i]) and (arr[i]==2*arr[j])):
                return True 
    return False
            

checkIfExist([-20,8,-6,-14,0,-19,14,4])