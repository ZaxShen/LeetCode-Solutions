# Last updated: 8/4/2025, 10:45:10 PM
class Solution:
    def finalPrices(self, prices: List[int]) -> List[int]:
        stack = []

        for i, price in enumerate(prices):
            while stack and prices[stack[-1]] >= price:
                last_greatest = stack.pop()
                prices[last_greatest] -= price
            stack.append(i)

        return prices