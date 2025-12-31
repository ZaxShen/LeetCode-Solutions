# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode(0, head)
        prev = dummy
        
        while prev.next and prev.next.next:
            # Init the pair to swap
            first = prev.next
            second = first.next

            # Swap
            prev.next = second
            first.next = second.next
            second.next = first

            # Next round
            prev = first

        return dummy.next

