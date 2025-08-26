class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next:
            return head
        
        dummy = ListNode(0)
        dummy.next = head
        
        curr = head
        while curr.next:
            # Pull next node to the front
            temp = curr.next
            curr.next = temp.next
            temp.next = dummy.next
            dummy.next = temp
        
        return dummy.next