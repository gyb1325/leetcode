class Solution:

    def rangeBitwiseAnd(self, m: int, n: int) -> int:
        step = 0
        while m != n:
            m >>= 1
            n >>= 1
            step += 1
        return m << step
