def sortArrayByParity(nums):
        pos=0
        for i in range(len(nums)):
            l=nums[i]
            if l%2==0:
                nums[pos],nums[i]=nums[i],nums[pos]
                pos+=1
        return nums
print(sortArrayByParity([2,1,3,5,6]))