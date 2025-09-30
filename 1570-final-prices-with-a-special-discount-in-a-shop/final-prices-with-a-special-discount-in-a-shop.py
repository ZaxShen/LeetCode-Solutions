class Solution:
    def finalPrices(self, prices: List[int]) -> List[int]:
        asc = []

        for i, v in enumerate(prices):
            while asc and prices[asc[-1]] >= v:
                j = asc.pop()
                prices[j] -= v
            asc.append(i)

        return prices