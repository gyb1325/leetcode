class Solution:

    def findMin(self, nums: List[int]) -> int:
        left = 0
        right = len(nums) - 1
        temp = nums[0]
        while left < right:
            mid = left + (right - left) // 2
            if nums[mid] < nums[right]:
                right = mid
            elif nums[mid] > nums[right]:
                left = mid + 1
            else:
                right -= 1
        return nums[left]
        # May a little bit faster
        # left = 0
        # right = len(nums) - 1
        # temp = nums[0]
        # while left < right and nums[left] >= nums[right]:
        #     mid = left + (right - left) // 2
        #     if nums[mid] < nums[right]:
        #         right = mid
        #     elif nums[mid] > nums[right]:
        #         left = mid + 1
        #     else:
        #         right -=1
        #         left += 1
        # return nums[left]
