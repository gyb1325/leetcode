class Solution:

    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        m = len(obstacleGrid)
        n = len(obstacleGrid[0])
        aux = [[0] * n for _ in range(m)]
        aux[0][0] = 1 * (1 - obstacleGrid[0][0])
        for i in range(1, m):
            aux[i][0] = aux[i - 1][0] * (1 - obstacleGrid[i][0])
        for j in range(1, n):
            aux[0][j] = aux[0][j - 1] * (1 - obstacleGrid[0][j])
        for i in range(1, m):
            for j in range(1, n):
                if obstacleGrid[i][j] != 1:
                    aux[i][j] = aux[i - 1][j] + aux[i][j - 1]
        return aux[-1][-1]
