class Solution:

    def maxProfit(self, k: int, prices: List[int]) -> int:
        if k == 0:
            return 0
        if not prices:
            return 0
        if k > len(prices) // 2:
            return self.quicksolve(prices)
        hold = [float("-inf")] * k
        release = [0] * k
        for p in prices:
            for i in range(k - 1, -1, -1):
                if i > 0:
                    release[i] = max(release[i], hold[i] + p)
                    hold[i] = max(hold[i], release[i - 1] - p)
                else:
                    release[i] = max(release[i], hold[i] + p)
                    hold[i] = max(hold[i],  -p)
        return release[-1]

    def quicksolve(self, prices):
        prev = prices[0]
        res = 0
        for p in prices[1:]:
            if p > prev:
                res += p - prev
            prev = p
        return res
