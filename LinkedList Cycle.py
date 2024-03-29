"""You might have come up with the solution using the hash table. But there is a more efficient solution using the two-pointer technique. Try to think it over by yourself before reading the remaining content.

Imagine there are two runners with different speed. If they are running on a straight path, the fast runner will first arrive at the destination. However, if they are running on a circular track, the fast runner will catch up with the slow runner if they keep running.

That's exactly what we will come across using two pointers with different speed in a linked list:

If there is no cycle, the fast pointer will stop at the end of the linked list.
If there is a cycle, the fast pointer will eventually meet with the slow pointer."""


"""It is a safe choice to move the slow pointer one step at a time while moving the fast pointer two steps at a time.
 For each iteration, the fast pointer will move one extra step. 
 If the length of the cycle is M, after M iterations, the fast pointer will definitely move one more cycle and 
 catch up with the slow pointer."""

 class Solution:
    def hasCycle(head):    # Space complexity is O(1) Time complexity O(n) Twopointer
        slow=fast=head

        while slow and fast and fast.next:
            slow=slow.next
            fast=fast.next.next
            if slow==fast:
                return True
        return False


class Solution:
    def hasCycle(head):    # Space complexity is O(n) Time complexity O(n) Hashset

        seen=set()
        cur=head
        while cur:
            if cur in seen:
                return True
            seen.add(cur)
            cur=cur.next
        return False
        