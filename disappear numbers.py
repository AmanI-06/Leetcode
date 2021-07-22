def findDisappearedNumbers(nums):
        s=set(nums)
        for i in range(1,len(nums)+1):
            if i in s:
                s.remove(i)
            else:
                s.add(i)
        return list(s)
print(findDisappearedNumbers([4,3,2,7,8,2,3,1]))
