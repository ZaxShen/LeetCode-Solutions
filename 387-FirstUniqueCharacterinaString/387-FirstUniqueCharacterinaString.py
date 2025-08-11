# Last updated: 8/11/2025, 12:20:14 AM
class Solution:
	# O(n), O(26)
    def firstUniqChar(self, s: str) -> int:
        counter = {}
        for char in s:
            counter[char] = counter.get(char, 0) + 1
        min_count = min(counter, key=counter.get)
        
        return s.index(min_count) if counter[min_count] == 1 else -1