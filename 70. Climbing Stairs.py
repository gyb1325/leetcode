class Solution:

    def climbStairs(self, n: int) -> int:
        # step = [0] * (n+1)
        # step[0] = 1
        # step[1] = 1
        # for i in range(2, n+1):
        #     step[i] = step[i-1] + step[i-2]
        # return step[-1]
        if n == 1:
            return 1
        prev = 1
        prev_prev = 1
        cur = 0
        for i in range(2, n + 1):
            cur = prev + prev_prev
            prev_prev = prev
            prev = cur
        return cur
