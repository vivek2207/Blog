    def reverseList(self, head: ListNode) -> ListNode:
        prev=None
        current=head
        Next=None
        while current!=None:
            Next=current.next
            current.next=prev
            prev=current
            current=Next
        
        head=prev
        return head
        
