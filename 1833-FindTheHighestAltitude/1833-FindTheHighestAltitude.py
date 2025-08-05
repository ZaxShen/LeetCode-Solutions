# Last updated: 8/4/2025, 10:44:12 PM
class Solution:
    # O(n), O(n)
    def largestAltitude(self, gain: list[int]) -> int:
        gain = [0] + gain
        acc = []
        curr = 0
        for i in range(len(gain)):
            curr += gain[i]
            acc.append(curr)

        return max(acc)