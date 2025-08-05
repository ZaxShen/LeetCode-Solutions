# Last updated: 8/4/2025, 10:45:36 PM
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    # O(n), O(1)
    def reverseList(self, head: ListNode) -> ListNode:
        prev = None
        curr = head

        while curr:
            curr.next, prev, curr = prev, curr, curr.next

        return prev

    # O(n), O(1)
    def getDecimalValue(self, head: ListNode) -> int:
        curr = self.reverseList(head)

        result = 0
        n_digits = 0
        while curr:
            if curr.val == 1:
                result += 2**n_digits
            curr = curr.next
            n_digits += 1

        return result