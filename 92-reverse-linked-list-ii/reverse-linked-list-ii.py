class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        if not head or left == right: return head
        
        # Step 1: Dummy node to handle head changes
        dummy = ListNode(0, head)
        prev = dummy
        
        # Step 2: Move 'pre' to the node at position (left - 1)
        for _ in range(left - 1):
            prev = prev.next
            
        # Step 3: Start the reversal process
        # 'start' is the node at the 'left' position
        # 'then' is the node that will be moved
        start = prev.next
        then = start.next
        
        # Step 4: Perform (right - left) swaps
        for _ in range(right - left):
            start.next = then.next
            then.next = prev.next
            prev.next = then

            then = start.next
            
        return dummy.next