""" def getPairsCount(arr, k): #brute force
        c=0
        for i in range(0,len(arr)):
            for j in range(i+1,len(arr)):
                if arr[i]+arr[j]==k:
                    c=c+1
        print(c) """



def getPairsCount(nums, target):
    complementmap=dict()
    for i in range(len(nums)):
        num=nums[i]
        complemt=target-num
        if num in complementmap:
            return [complementmap[num],i]
        else:
            complementmap[complemt]-i



a=[1,5,7,1]
j=6
print(getPairsCount(a,j))
