def findDuplicate(self, nums):
        """
        :type nums: List[int]   # using cyclic linked list and tortise method where slow moves 1 step and fast moves 2 steps
        :rtype: int
        """
        if len(nums) > 1:
            slow = nums[0]
            fast = nums[nums[0]]
            while slow != fast:
                slow = nums[slow]
                fast = nums[nums[fast]]
            fast = 0
            while slow != fast:
                slow = nums[slow]
                fast = nums[fast]
            return slow
        
        return -1