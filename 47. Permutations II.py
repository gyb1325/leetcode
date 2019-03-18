class Solution:

    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        if not nums:
            return []
        if len(nums) == 1:
            return [nums]
        nums.sort()
        res = []
        self.backtracking(nums, [], res)
        return res

    def backtracking(self, nums, path, res):
        if nums == []:
            res.append(path)
            return
        prev = float("inf")
        for i in range(len(nums)):
            if nums[i] == prev:
                continue
            else:
                prev = nums[i]
                self.backtracking(nums[:i] + nums[i + 1:], path + [nums[i]], res)
