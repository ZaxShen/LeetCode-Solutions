# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        dummy = ListNode(0, head)
        # Get the second half of list
        slow = fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        # Reverse seond half of list
        prev = None
        curr = slow
        while curr:
            curr.next, prev, curr = prev, curr, curr.next

        # Record List
        first = head
        second = prev
        # while first and second:
        while second.next:
            first.next, first = second, first.next
            second.next, second = first, second.next

        # return dummy.next
        return head
