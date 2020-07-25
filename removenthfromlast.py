    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        
        fast=head
        slow=head
        
        for i in range(n):
            if fast.next==None:
                head=head.next
                return head
            fast=fast.next
        
        while fast.next!=None:
            slow=slow.next
            fast=fast.next
        
        slow.next=slow.next.next
        
        return head
