# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode(0)
        dummy.next = head
        prev = dummy

        while prev.next and prev.next.next:
            # Init the pair to swap
            first = prev.next
            second = first.next

            # Perform the swap
            # prev.next = second  # Connect previous part
            # first.next = second.next  # Preserve connection to rest
            # second.next = first  # Complete swap

            first.next = second.next
            prev.next = second
            second.next = first

            # Move prev to end of swapped pair
            prev = first

        return dummy.next