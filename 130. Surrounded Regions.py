class Solution:

    def solve(self, board):
        """
        :type board: List[List[str]]
        :rtype: void Do not return anything, modify board in-place instead.
        """
        if not board:
            return
        m = len(board)
        n = len(board[0])

        save = [ij for k in range(max(m, n)) for ij in ((0, k), (k, 0), (m - 1, k), (k, n - 1))]
        while save:
            i, j = save.pop()
            if 0 <= i <= m - 1 and 0 <= j <= n - 1 and board[i][j] == "O":
                board[i][j] = "F"
                save += (i - 1, j), (i + 1, j), (i, j - 1), (i, j + 1)
        for row in board:
            for i, v in enumerate(row):
                row[i] = "XO"[v == "F"]
