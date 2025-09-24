class Solution:
    def maxNumberOfBalloons(self, text: str) -> int:
        balloon = {
            "b": 0,
            "a": 0,
            "l": 0,
            "o": 0,
            "n": 0
        }

        for char in text:
            if char in balloon:
                balloon[char] += 1

        ban = min(balloon['b'], balloon['a'], balloon['n'])
        lo = min(balloon['l'], balloon['o']) // 2
        
        return min(ban, lo)