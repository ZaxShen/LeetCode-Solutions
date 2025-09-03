class Solution:
    # O(n), O(1)
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        # Create dummy node to simplify edge cases
        dummy = ListNode(0, head)
        
        # Find the node just before the reversal section
        prev = dummy
        for _ in range(left - 1):
            prev = prev.next
        
        # Identify key node
        start = prev.next  # First node to reverse

        # Reverse the sublist using "move to front" technique
        for _ in range(right - left):
            curr = start.next  # Current node being processed
            curr.next, prev.next, start.next = prev.next, curr, curr.next
        
        return dummy.next