class Solution:
    def finalPrices(self, prices: List[int]) -> List[int]:
        non_desc_stack = []

        for idx, i in enumerate(prices):
            while non_desc_stack and prices[non_desc_stack[-1]] >= i:
                _ = non_desc_stack.pop()
                discount_price = prices[_] - i
                prices[_] = discount_price
            non_desc_stack.append(idx)

        return prices
            