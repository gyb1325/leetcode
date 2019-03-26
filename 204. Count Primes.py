class Solution:

    def countPrimes(self, n: int) -> int:
        notPrime = [False] * n
        cnt = 0
        for i in range(2, n):
            if not notPrime[i]:
                cnt += 1
                j = 2
                while j * i < n:
                    notPrime[i * j] = True
                    j += 1
        return cnt
