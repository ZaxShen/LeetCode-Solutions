# Last updated: 8/4/2025, 10:43:44 PM
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseEvenLengthGroups(self, head: Optional[ListNode]) -> Optional[ListNode]:
        def reverseBetween(connector: ListNode, group_count: int) -> ListNode:
            l = connector
            m = l.next
            for _ in range(group_count - 1):
                r = m.next
                l.next, m.next, r.next = r, r.next, l.next

            return m

        dummy = ListNode(-1, head)
        curr = head

        group_size = group_count = 1
        while curr:
            if group_count == group_size or not curr.next:
                if group_count % 2 == 0:
                    curr = reverseBetween(connector, group_count)
                connector = curr
                group_count = 0
                group_size += 1
            curr = curr.next
            group_count += 1
        
        return dummy.next