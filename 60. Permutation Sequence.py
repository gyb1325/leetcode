class Solution:

    def getPermutation(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: str
        """
        def helper(key):
            if key <= 1:
                return 1
            else:
                return key * helper(key - 1)
        res = []
        temp = [i for i in range(1, n + 1)]
        k -= 1
        while n > 0:
            n -= 1
            a = k // helper(n)
            k = k % helper(n)
            res.append(temp[a])
            temp.remove(temp[a])

        return "".join(str(i) for i in res)
