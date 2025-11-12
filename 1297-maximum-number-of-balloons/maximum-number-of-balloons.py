class Solution:
    def maxNumberOfBalloons(self, text: str) -> int:
        balloon = {
            'b': 0,
            'a': 0,
            'l': 0,
            'o': 0,
            'n': 0
        }

        for i in text:
            if i in balloon:
                balloon[i] += 1

        one_letter = balloon[min(balloon, key=balloon.get)]
        two_letter = min(balloon['l'], balloon['o']) // 2

        return min(one_letter, two_letter)