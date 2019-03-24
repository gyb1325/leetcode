class Solution:

    def calculateMinimumHP(self, dungeon: List[List[int]]) -> int:
        m = len(dungeon)
        n = len(dungeon[0])
        aux = [[float("inf")] * (n + 1) for _ in range(m + 1)]
        aux[m][n - 1] = 1
        aux[m - 1][n] = 1
        for i in range(m - 1, -1, -1):
            for j in range(n - 1, -1, -1):
                aux[i][j] = max(min(aux[i + 1][j], aux[i][j + 1]) - dungeon[i][j], 1)
        return aux[0][0]
