# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        dummy = prev = ListNode(0, head)
        for _ in range(left - 1):
            prev = prev.next

        # prev = 1
        # curr = 2
        curr = prev.next
        for _ in range(right - left):
            tmp = curr.next

            curr.next = tmp.next
            tmp.next = prev.next
            prev.next = tmp

        return dummy.next