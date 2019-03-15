class Solution:

    def maxProfit(self, prices: List[int]) -> int:
        if not prices:
            return 0
        pre = prices[0]
        max_profit = 0
        for price in prices[1:]:
            if price > pre:
                max_profit += price - pre
            pre = price
        return max_profit
