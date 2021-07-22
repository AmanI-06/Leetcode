def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> ListNode:
        seen=set()
        cur1=headA        #memory O(n)
        cur2=headB
        while cur1:
            seen.add(cur1) 
            cur1=cur1.next
            
        while cur2:
            if cur2 in seen:
                return cur2
            cur2=cur2.next
        return None



class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> ListNode:
        
        tempA = headA            #memeory o(1)
        tempB = headB
           
        countA =0
        countB =0
        while tempA is not None:
            countA+=1
            tempA = tempA.next
            
        while tempB is not None:
            countB+=1
            tempB = tempB.next
        
   
        diff = abs(countA-countB)
 
        if countA>countB:
            while diff:
                headA =  headA.next
                diff-=1
             
        if countA<countB:
            while diff:
                headB =  headB.next
                diff-=1
        
        while headA is not None:
            if headA == headB:
                
                return headA
            
            headA = headA.next
            headB = headB.next
            
            

