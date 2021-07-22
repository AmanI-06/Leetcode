def thirdMax(nums):
        print(set(nums))
        numss = sorted(set(nums),reverse=True)
        print(numss)
        if len(numss) < 3:
            return numss[0]
        else:
            return numss[2]

print(thirdMax([5,5,4,4,3,3,2,2]))

