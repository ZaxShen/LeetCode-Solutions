# Last updated: 8/4/2025, 10:43:41 PM
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:
        slow, fast = head, head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        prev, curr = None, slow
        while curr:
            # prev, curr, curr.next = curr, curr.next, prev
            prev, curr.next, curr = curr, prev, curr.next
        
        first, second = head, prev
        res = 0
        while first and second:
            res = max(res, first.val + second.val)
            first = first.next
            second = second.next

        return res
