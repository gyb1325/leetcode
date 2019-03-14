class Solution:

    def numDistinct(self, s: str, t: str) -> int:
        m = len(s)
        n = len(t)
        aux = [[0] * (n + 1) for _ in range(m + 1)]
        for i in range(m + 1):
            aux[i][0] = 1

        for j in range(1, n + 1):
            for i in range(1, m + 1):
                if s[i - 1] != t[j - 1]:
                    aux[i][j] = aux[i - 1][j]
                else:
                    aux[i][j] = aux[i - 1][j - 1] + aux[i - 1][j]
        return aux[-1][-1]
