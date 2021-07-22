def dominantIndex(nums):
        if len(nums) == 1:
            return 0
        
        max_num = max(nums)
        max_index = 0
        for i in range(len(nums)):
            if nums[i] == max_num:
                max_index = i
            elif nums[i] == 0:
                continue
            elif nums[i] * 2 > max_num:
                return -1
            
        return max_index
print(dominantIndex([3,6,1,0]))