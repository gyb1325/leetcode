class Solution:

    def singleNumber(self, nums: List[int]) -> int:
        final = nums[0]
        n = len(nums)
        for i in range(1, n):
            final ^= nums[i]
        return final
