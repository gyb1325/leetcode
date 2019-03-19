class Solution:

    def maxSubArray(self, nums: List[int]) -> int:
        curSum = nums[0]
        maxSum = nums[0]
        for n in nums[1:]:
            curSum = n + curSum if curSum > 0 else n
            maxSum = max(maxSum, curSum)
        return maxSum
