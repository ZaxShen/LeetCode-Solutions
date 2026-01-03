# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        dummy = ListNode(0, head)
        prev = dummy
        for _ in range(left - 1):
            prev = prev.next

        start = prev.next
        for _ in range(right - left):
            curr = start.next

            start.next = curr.next
            curr.next = prev.next
            prev.next = curr

        return dummy.next
            