"""class Solution:
    def isPalindrome(self, head: ListNode) -> bool:      O(n) and O(n)
        nums=[]
        
        while head:
            nums.append(head.val)
            head=head.next
            
        l,r=0,len(nums)-1
        while l<=r:
            if nums[l]!=nums[r]:
                return False
            l+=1
            r-=1
            
        return True
"""
"""
    def isPalindrome(self, head: ListNode) -> bool:
        slow,fast=head
        
        while head and head.next:
            fast=fast.next.next
            slow=slow.next

        
        prev=None
        while slow:
            tmp=slow.next    
            slow.next=prev
            prev=slow
            slow=temp

        left,right=head,prev
        while right:
            if right.val != left.val:
                return Flase
            left=left.next
            right=right.next
            return True  

                                                                                                     



https://www.youtube.com/watch?v=yOzXms1J6Nk






                                                                                            """