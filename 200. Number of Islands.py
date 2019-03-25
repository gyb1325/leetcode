class Solution:

    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid:
            return 0
        self.m = len(grid)
        self.n = len(grid[0])
        cnt = 0
        for i in range(self.m):
            for j in range(self.n):
                if grid[i][j] == "1":
                    self.dfs(grid, i, j)
                    cnt += 1
        return cnt

    def dfs(self, grid, i, j):
        if i < 0 or j < 0 or i >= self.m or j >= self.n or grid[i][j] != "1":
            return
        grid[i][j] = "#"
        self.dfs(grid, i - 1, j)
        self.dfs(grid, i + 1, j)
        self.dfs(grid, i, j - 1)
        self.dfs(grid, i, j + 1)
