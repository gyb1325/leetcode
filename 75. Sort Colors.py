class Solution:

    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        l, r, ptr = 0, len(nums) - 1, 0

        while ptr <= r:
            if nums[ptr] == 0:
                nums[l], nums[ptr] = nums[ptr], nums[l]
                l += 1
                ptr += 1
            elif nums[ptr] == 2:
                nums[r], nums[ptr] = nums[ptr], nums[r]
                r -= 1
            else:
                ptr += 1
