class Solution:

    def trailingZeroes(self, n: int) -> int:
        res = 0
        temp = 5
        while n // temp > 0:
            res += n // temp
            temp *= 5
        return res
