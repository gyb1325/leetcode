class Solution:

    def missingNumber(self, nums: List[int]) -> int:
        n = len(nums)
        nums.append(n + 1)
        for i in range(n):
            nums[abs(nums[i])] *= -1
        for i in range(n + 1):
            if nums[i] > 0:
                return i
        for i in range(n + 1):
            if nums[i] == 0:
                return i
