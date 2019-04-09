class Solution:

    def productExceptSelf(self, nums: List[int]) -> List[int]:
        res = [1]
        for i in range(1, len(nums)):
            res.append(res[-1] * nums[i - 1])
        prev = 1
        for i in range(len(nums) - 2, -1, -1):
            prev *= nums[i + 1]
            res[i] = res[i] * prev
        return res
