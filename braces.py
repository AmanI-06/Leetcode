def matched(s):
    count=0
    for c in s:
        if (c ==')'):
            count-=1
        if (c=='('):
            count+=1
        if count<0:
            return False
    if count==0:
        return True
    else:
        return False

print(matched("a)*(?"))