class Solution:

    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        res = []
        self.helper([i for i in range(1, 10)], k, n, 0, [], res)
        return res

    def helper(self, nums, k, n, index, path, res):
        if k < 0 or n < 0:
            return
        if k == 0 and n == 0:
            res.append(path)
            return
        for i in range(index, 9):
            self.helper(nums, k - 1, n - nums[i], i + 1, path + [nums[i]], res)
