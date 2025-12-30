class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        # Step 1: Find the middle using Fast/Slow pointers
        fast = slow = head
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next
            
        # Step 2: Reverse the second half
        prev = None
        while slow:
            temp = slow.next
            slow.next = prev
            prev = slow
            slow = temp
            
        # Step 3: Check palindrome
        left, right = head, prev
        while right: # Only need to check the reversed half
            if left.val != right.val:
                return False
            left = left.next
            right = right.next
            
        return True