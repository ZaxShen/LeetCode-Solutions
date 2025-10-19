class Solution:
    def finalPrices(self, prices: List[int]) -> List[int]:
        stack_x_desc = []

        for idx, i in enumerate(prices):
            while stack_x_desc and prices[stack_x_desc[-1]] >= i:
                prices[stack_x_desc.pop()] -= i
            stack_x_desc.append(idx)

        return prices
            