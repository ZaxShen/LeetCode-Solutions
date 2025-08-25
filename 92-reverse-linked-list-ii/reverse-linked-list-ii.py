# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        # Create dummy node to simplify edge cases
        dummy = ListNode(0, head)
        
        # Find the node just before the reversal section
        prev = dummy
        for _ in range(left - 1):
            prev = prev.next
        
        # Reverse by repeatedly moving nodes to the front
        curr = prev.next
        for _ in range(right - left):
            # Extract the next node
            temp = curr.next
            # curr.next = temp.next
            
            # Move it to the front of the reversed section
            # temp.next = prev.next
            # prev.next = temp
            # curr.next, temp.next, prev.next = temp.next, prev.next, temp
            temp.next, prev.next, curr.next = prev.next, temp, temp.next
        
        return dummy.next