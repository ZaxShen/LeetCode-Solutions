class Solution:
    def finalPrices(self, prices: List[int]) -> List[int]:
        asc_stack = []

        for idx, i in enumerate(prices):
            while asc_stack and prices[asc_stack[-1]] >= i:
                prices[asc_stack.pop()] -= i
            asc_stack.append(idx)

        return prices