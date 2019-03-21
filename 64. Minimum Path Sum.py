class Solution:

    def minPathSum(self, grid: 'List[List[int]]') -> 'int':
        m = len(grid)
        n = len(grid[0])
        aux = [[0] * n for _ in range(m)]
        aux[0][0] = grid[0][0]
        for i in range(m):
            for j in range(n):
                if i - 1 >= 0 and j - 1 >= 0:
                    aux[i][j] = min(aux[i - 1][j], aux[i][j - 1]) + grid[i][j]
                elif i - 1 >= 0:
                    aux[i][j] = aux[i - 1][j] + grid[i][j]
                elif j - 1 >= 0:
                    aux[i][j] = aux[i][j - 1] + grid[i][j]
        return aux[-1][-1]
