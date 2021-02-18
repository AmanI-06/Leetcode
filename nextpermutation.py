def nextperm(l):
    lenth=len(l)
    if lenth<=2:
        return l.reverse()
    pointer=lenth-2

    while pointer>=0 and l[pointer] >=l[pointer+1]:
        pointer-=1

    if pointer == -1:
        return l.reverse()

    for x in range(lenth-1,pointer,-1):
        if l[pointer]< l[x]:
            l[pointer],l[x]=l[x],l[pointer]
            break

    l[pointer+1:]=reversed(l[pointer+1:])

h=[1,2,3,5,6,7]
print(nextperm(h))






    