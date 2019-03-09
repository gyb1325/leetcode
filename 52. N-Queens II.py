class Solution:

    def totalNQueens(self, n: int) -> int:
        res = [0]
        self.dfs([-1] * n, 0, [], res)
        return res[0]

    def dfs(self, nums, index, path, res):
        if index == len(nums):
            res[0] += 1
            return
        for i in range(len(nums)):
            nums[index] = i
            if self.isValid(nums, index):
                temp = "." * len(nums)
                self.dfs(nums, index + 1, path + [temp[:i] + "Q" + temp[i + 1:]], res)

    def isValid(self, nums, index):
        for i in range(index):
            if abs(nums[i] - nums[index]) == index - i or nums[i] == nums[index]:
                return False
        return True
