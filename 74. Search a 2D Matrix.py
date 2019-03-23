class Solution:

    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        m = len(matrix)
        if m == 0:
            return False
        n = len(matrix[0])

        if n == 0:
            return False
        row = []
        for i in range(m):
            row.append(matrix[i][0])

        # row search
        idx, flag = self.helper(row, 0, m - 1, target)
        if flag:
            return True

        idx, flag = self.helper(matrix[idx], 0, n - 1, target)

        return flag

    def helper(self, lst, start, end, target):
        if start > end:
            return start - 1, False
        mid = (start + end) // 2
        if target == lst[mid]:
            return mid, True
        if target > lst[mid]:
            return self.helper(lst, mid + 1, end, target)
        else:
            return self.helper(lst, start, mid - 1, target)
