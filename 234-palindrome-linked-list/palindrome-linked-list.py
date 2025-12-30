class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        # Step 1: Find the middle using Fast/Slow pointers
        fast = slow = head
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next
            
        # Step 2: Reverse the second half
        prev, curr = None, slow
        while curr:
            curr.next, prev, curr = prev, curr, curr.next

        # Step 3: Check palindrome
        first, second = head, prev
        while second:  # Only need to check the reversed half
            if first.val != second.val:
                return False
            first = first.next
            second = second.next
            
        return True