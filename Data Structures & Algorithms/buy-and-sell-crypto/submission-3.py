class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        res = 0
        minbuy = prices[0]

        for prix in prices:
            profit = prix - minbuy
            minbuy = min(minbuy, prix)
            res = max(res, profit)
        return res
        