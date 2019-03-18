class Solution:

    def permute(self, nums: List[int]) -> List[List[int]]:
        if not nums:
            return []
        if len(nums) == 1:
            return [nums]
        res = []
        self.backtracking(nums, [], {}, res)
        return res

    def backtracking(self, nums, path, dic, res):
        if len(path) == len(nums):
            res.append(path)
        for num in nums:
            if num in dic:
                continue
            else:
                dic[num] = 0
                self.backtracking(nums, path + [num], dic, res)
                del dic[num]
