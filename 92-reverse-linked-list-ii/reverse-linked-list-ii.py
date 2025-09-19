# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        dummy = ListNode(0, head)
        prev = dummy
        
        for _ in range(left - 1): # 2, (0)
            prev = prev.next
        
        curr = prev.next
        for _ in range(right - left):
            tmp = curr.next # 1 3 2 4 5

            # prev.next = tmp
            # tmp.next = prev.next
            # curr.next = tmp.next

            tmp.next, prev.next, curr.next = prev.next, tmp, tmp.next

        return dummy.next
