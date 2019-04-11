class Solution:

    def nthUglyNumber(self, n: int) -> int:
        n2, n3, n5 = 0, 0, 0
        ugly = [1]
        while n > 1:
            umin = min(ugly[n2] * 2, ugly[n3] * 3, ugly[n5] * 5)
            if umin == ugly[n2] * 2:
                n2 += 1
            if umin == ugly[n3] * 3:
                n3 += 1
            if umin == ugly[n5] * 5:
                n5 += 1
            ugly.append(umin)
            n -= 1
        return ugly[-1]
