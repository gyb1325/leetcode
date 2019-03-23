class Solution:

    def minDistance(self, word1: str, word2: str) -> int:
        m = len(word1)
        n = len(word2)
        aux = [[0] * (n + 1) for _ in range(m + 1)]

        for i in range(m + 1):
            aux[i][0] = i
        for j in range(n + 1):
            aux[0][j] = j

        for i in range(1, m + 1):
            for j in range(1, n + 1):
                step = int(word1[i - 1] != word2[j - 1])
                aux[i][j] = min(1 + aux[i - 1][j], 1 + aux[i][j - 1], step + aux[i - 1][j - 1])
        return aux[-1][-1]
