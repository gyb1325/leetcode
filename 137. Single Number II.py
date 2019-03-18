class Solution:

    def singleNumber(self, nums: List[int]) -> int:
        # O(n) Space
        # return  (sum(set(nums)) * 3 - sum(nums))//2
        # O(1) space
        ones = 0
        twos = 0
        for i in range(len(nums)):
            ones = (ones ^ nums[i]) & (~twos)
            twos = (twos ^ nums[i]) & (~ones)
        return ones
