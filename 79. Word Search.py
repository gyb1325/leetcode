class Solution:

    def exist(self, board: List[List[str]], word: str) -> bool:
        m = len(board)
        n = len(board[0])
        for i in range(m):
            for j in range(n):
                if self.helper(board, i, j, word):
                    return True
        return False

    def helper(self, board, i, j, word):
        if not word:
            return True

        if i < 0 or j < 0 or i >= len(board) or j >= len(board[0]) or board[i][j] != word[0]:
            return False
        temp = board[i][j]
        board[i][j] = "#"
        flag = self.helper(board, i + 1, j, word[1:]) or self.helper(board, i - 1, j, word[1:]
                                                                     ) or self.helper(board, i, j + 1, word[1:]) or self.helper(board, i, j - 1, word[1:])

        board[i][j] = temp
        return flag
