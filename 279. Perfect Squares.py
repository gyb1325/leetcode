class Solution:

    def numSquares(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n == 1:
            return 1

        lst = []
        i = 1
        while i**2 <= n:
            lst.append(i**2)
            i += 1

        chklist = {n}
        cnt = 0
        while chklist:
            cnt += 1
            temp = set()
            for x in chklist:
                for y in lst:
                    if x == y:
                        return cnt
                    if x < y:
                        break
                    temp.add(x - y)
            chklist = temp


v = {0: 0}


class Solution:

    def numSquares(self, n: int) -> int:
        if n == 0:
            return 0
        if n in v:
            return v[n]
        j = 1
        min_numS = float("inf")
        while j * j <= n:
            min_numS = min(min_numS, self.numSquares(n - j * j) + 1)
            j += 1
        v[n] = min_numS
        return min_numS
