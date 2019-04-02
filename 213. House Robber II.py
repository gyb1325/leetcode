class Solution:

    def rob(self, nums: List[int]) -> int:
        if not nums:
            return 0
        n = len(nums)
        if n == 1:
            return nums[0]
        prev = 0
        cur = 0
        for i in range(n - 1):
            cur, prev = max(prev + nums[i], cur), cur
        cur_max = cur
        prev = 0
        cur = 0
        for i in range(1, n):
            cur, prev = max(prev + nums[i], cur), cur
        return max(cur_max, cur)
