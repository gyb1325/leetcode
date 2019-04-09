class Solution:

    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        prev = 1
        res = [1]
        for i in range(1, len(nums)):
            prev = prev * nums[i - 1]
            res.append(prev)
        prev = 1
        for i in range(len(nums) - 2, -1, -1):
            prev = prev * nums[i + 1]
            res[i] = res[i] * prev
        return res
