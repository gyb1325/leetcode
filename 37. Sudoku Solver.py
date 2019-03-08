class Solution:

    def solveSudoku(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        self.board = board
        self.solve()

    def find_unsolved(self):
        for i in range(9):
            for j in range(9):
                if self.board[i][j] == ".":
                    return i, j
        return -1, -1

    def solve(self):
        row, col = self.find_unsolved()
        if row == -1 and col == -1:
            return True
        nums = ['1', '2', '3', '4', '5', '6', '7', '8', '9']
        for num in nums:
            if self.isSafe(row, col, num):
                self.board[row][col] = num
                if self.solve():
                    return True
                self.board[row][col] = "."
        return False

    def isSafe(self, row, col, num):
        square_row = row - row % 3
        square_col = col - col % 3
        if self.check_row(row, num) and self.check_col(col, num) and self.check_square(square_row, square_col, num):
            return True
        return False

    def check_row(self, row, num):
        for i in range(9):
            if self.board[row][i] == num:
                return False
        return True

    def check_col(self, col, num):
        for i in range(9):
            if self.board[i][col] == num:
                return False
        return True

    def check_square(self, row, col, num):
        for i in range(row, row + 3):
            for j in range(col, col + 3):
                if self.board[i][j] == num:
                    return False
        return True
