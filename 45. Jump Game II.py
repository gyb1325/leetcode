class Solution:

    def jump(self, nums: List[int]) -> int:
        n = len(nums)
        start = 0
        end = 0
        step = 0
        while end < n - 1:
            step += 1
            maxend = 0
            for i in range(start, end + 1):
                if nums[i] + i >= n - 1:
                    return step
                maxend = max(maxend, nums[i] + i)
            start, end = end + 1, maxend
        return step
