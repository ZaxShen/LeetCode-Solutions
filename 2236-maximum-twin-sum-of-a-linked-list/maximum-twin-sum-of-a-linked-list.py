# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:
        slow = fast = head
        # slow, fast = head, head
        while fast and fast.next:
            slow, fast = slow.next, fast.next.next

        prev, curr = None, slow
        while curr:
            curr.next, prev, curr = prev, curr, curr.next

        res = -float('inf')
        first, second = head, prev
        while first and second:
            pair = first.val + second.val
            res = max(res, pair)
            first, second = first.next, second.next

        return res