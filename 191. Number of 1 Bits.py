class Solution(object):

    def hammingWeight(self, n):
        """
        :type n: int
        :rtype: int
        """
        res = 0
        for _ in range(32):
            res += (n & 1)
            n = n >> 1
        return res


class Solution(object):

    def hammingWeight(self, n):
        """
        :type n: int
        :rtype: int
        """
        cnt = 0
        while n > 0:
            n = n & (n - 1)
            cnt += 1
        return cnt
