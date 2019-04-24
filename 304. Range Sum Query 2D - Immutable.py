class NumMatrix:

    def __init__(self, matrix: List[List[int]]):
        if not matrix:
            return
        m = len(matrix)
        n = len(matrix[0])
        self.mem = [[0] * (n + 1) for _ in range(m + 1)]
        # row accumulation:
        for i in range(1, m + 1):
            for j in range(1, n + 1):
                self.mem[i][j] = matrix[i - 1][j - 1] + self.mem[i][j - 1]
        for j in range(1, n + 1):
            for i in range(1, m + 1):
                self.mem[i][j] += self.mem[i - 1][j]

    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        return self.mem[row2 + 1][col2 + 1] - self.mem[row1][col2 + 1] - self.mem[row2 + 1][col1] + self.mem[row1][col1]


# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)
