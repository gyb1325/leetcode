class Solution:

    def maxProfit(self, prices: List[int]) -> int:
        low_price = prices[0]
        max_profit = 0
        for price in prices[1:]:
            low_price = min(low_price, price)
            profit = price - low_price
            max_profit = max(max_profit, profit)
        return max_profit
