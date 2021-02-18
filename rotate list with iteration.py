def rotatelist(arr,t):
    lst = arr[:]
    for i in range(t):
        temp = lst[0]
        lst.append(temp)
        lst.pop(0)
    return lst
f=[1,2,3,4,5]
print(rotatelist(f,3))



        