class Solution:
    def finalPrices(self, prices: List[int]) -> List[int]:
        asc = []

        for i, v in enumerate(prices):
            while asc and prices[asc[-1]] >= v:
                j = asc[-1]
                prices[j] -= v
                asc.pop()
            asc.append(i)

        return prices