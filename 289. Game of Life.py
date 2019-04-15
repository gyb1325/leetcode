class Solution:

    def gameOfLife(self, board):
        """
        :type board: List[List[int]]
        :rtype: void Do not return anything, modify board in-place instead.
        """
        m = len(board)
        n = len(board[0])
        for i in range(m):
            for j in range(n):
                if board[i][j] == 0 or board[i][j] == 2:
                    if self.check_liveness(board, i, j) == 3:
                        board[i][j] = 2
                else:
                    if self.check_liveness(board, i, j) < 2 or self.check_liveness(board, i, j) > 3:
                        board[i][j] = 3
        for i in range(m):
            for j in range(n):
                if board[i][j] == 2:
                    board[i][j] = 1
                elif board[i][j] == 3:
                    board[i][j] = 0

    def check_liveness(self, board, i, j):
        cnt = 0
        m = len(board)
        n = len(board[0])
        if (i - 1) >= 0 and (j - 1) >= 0:
            cnt += board[i - 1][j - 1] % 2
        if (i - 1) >= 0:
            cnt += board[i - 1][j] % 2
        if (i - 1) >= 0 and (j + 1) < n:
            cnt += board[i - 1][j + 1] % 2
        if (j - 1) >= 0:
            cnt += board[i][j - 1] % 2
        if (j + 1) < n:
            cnt += board[i][j + 1] % 2
        if (i + 1) < m and (j - 1) >= 0:
            cnt += board[i + 1][j - 1] % 2
        if (i + 1) < m:
            cnt += board[i + 1][j] % 2
        if (i + 1) < m and (j + 1) < n:
            cnt += board[i + 1][j + 1] % 2
        return cnt
