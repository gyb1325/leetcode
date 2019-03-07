class Solution:

    def numTrees(self, n: int) -> int:
        aux = [0] * (n + 1)
        aux[0] = 1
        aux[1] = 1
        for i in range(2, n + 1):
            for j in range(i):
                aux[i] += aux[j] * aux[i - j - 1]
        return aux[-1]
