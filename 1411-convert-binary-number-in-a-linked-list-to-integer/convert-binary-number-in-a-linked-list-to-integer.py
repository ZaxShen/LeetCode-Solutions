# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    # O(n), O(n)
    def getDecimalValue(self, head: Optional[ListNode]) -> int:
        l = []
        
        while head:
            l.append(head.val)
            head = head.next

        res = 0
        for idx, i in enumerate(l[::-1]):
            if i == 1:
                res += 2 ** idx

        return res