# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        node1, node2 = l1, l2
        dummy = curr = ListNode()
        carry = 0

        while node1 or node2 or carry:
            if node1:
                val1 = node1.val
                node1 = node1.next
            else:
                val1 = 0

            if node2:
                val2 = node2.val
                node2 = node2.next
            else:
                val2 = 0
            
            val = val1 + val2 + carry
            carry = val // 10
            curr.next = ListNode(val % 10)
            curr = curr.next

        return dummy.next

