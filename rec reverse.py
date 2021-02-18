def reverseList(A, start, end):
    if start >= end:
        return
    A[start], A[end] = A[end], A[start]
    reverseList(A, start+1, end-1)
 
# Driver function to test above function
if __name__=='__main__':
    a=list(input().split(' '))
    print(a)
    s=int(input())
    e=int(input())
    f=reverseList(a, s,e)
    print("Reversed list is")
    print(f)