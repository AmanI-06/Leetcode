def thirdMax(nums):
        try:
            return sorted(list(set(nums)))[-3]
        except:
            return sorted(list(set(nums)))[-1]
print(thirdMax([5,5,4,4,3,3,2,2]))
