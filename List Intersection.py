def intersection(nums1, nums2):
        k=[]
        f,h=list(set(nums1)),list(set(nums2))
        a=len(f)
        b=len(h)
        print(f,h)
        if a<=b:
            for i in range(len(nums2)):
                if nums2[i] in nums1:
                    k.append(nums2[i])
                else:
                    pass
        elif b<=a:
            for i in range(len(nums1)):
                if nums1[i] in nums2:
                    k.append(nums1[i])
                else:
                    pass
        return list(set(k))




"""res = []
    for i in nums1:
        if i not in res and i in nums2:
            res.append(i)
    
    return res


res = []
    map = {}
    for i in nums1:
        map[i] = map[i]+1 if i in map else 1
    for j in nums2:
        if j in map and map[j] > 0:
            res.append(j)
            map[j] = 0
    
    return res  """
    
print(intersection([9,4,9,8,4],[9,9,3]))


