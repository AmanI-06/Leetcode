import math
def majorityElement(nums):
        n=len(nums)
        max=nums[0]
        c=1
        for i in range(n):
            if nums[i]==max:
                c+=1
            else:
                c-=1
            if c==0:
                max=nums[i]
                c=1
        print(c)
        return max
print(majorityElement([3,2,3,3,3,3,3,3,66,6,6,6,6,6,6,8,8,8,8,8]))


""" def majorityElement(self, nums: List[int]) -> int:
        i=0
        f=int(math.ceil(len(nums)/2))
        for i in range(0,len(nums)):
            if nums.count(nums[i]) >=f:
                return nums[i]"""

   