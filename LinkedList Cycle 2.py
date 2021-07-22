class Solution:
    def detectCycle(self, head: ListNode) -> ListNode:
        slow,fast=head,head
        while fast and fast.next:
            slow=slow.next
            fast=fast.next.next
            if slow==fast:
                break
        else:
            return None
        
        poin=head
        while poin!=fast:
            poin=poin.next
            fast=fast.next
        return poin