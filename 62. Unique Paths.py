class Solution:

    def uniquePaths(self, m, n):
        """
        :type m: int
        :type n: int
        :rtype: int
        """
        aux = [[1 for x in range(m)] for y in range(n)]

        for i in range(1, m):
            for j in range(1, n):
                aux[j][i] = aux[j][i - 1] + aux[j - 1][i]
        return aux[-1][-1]
