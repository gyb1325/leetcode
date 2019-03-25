class Solution(object):

    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # O(n) Space
        # if not nums: return 0
        # n = len(nums)
        # if n == 1:return nums[0]
        # dp = [0] * n
        # dp[0] = nums[0]
        # for i in range(1,n):
        #     dp[i] = max(dp[i-2] + nums[i], dp[i-1])
        # return dp[-1]

        if not nums:
            return 0
        n = len(nums)
        prev = 0
        cur = 0
        for i in range(n):
            cur, prev = max(prev + nums[i], cur), cur
        return cur
