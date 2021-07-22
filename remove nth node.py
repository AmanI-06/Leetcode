class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        dummy=listnode(0,head)
        left=dummy
        right=head
        while n>0 and right:
            right=right.next
            n-=1

        while right:
            left=left.next
            right=right.next
        
        left.next=left.next.next
        return dummy.next

class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        nodes = []
        current = head
        while current:
            nodes.append(current)
            current = current.next
        if n > 1:
            if len(nodes) != n:
                nodes[len(nodes) - n - 1].next = nodes[len(nodes) - n + 1]
            else:
                head = head.next
        elif len(nodes) > 1:
            nodes[len(nodes) - n - 1].next = None
        else:
            return None
        return head