class Solution:

    def majorityElement(self, nums: List[int]) -> int:
        candidate = nums[0]
        cnt = 1
        for num in nums[1:]:
            if candidate == num:
                cnt += 1
            elif cnt == 0:
                candidate = num
                cnt = 1
            else:
                cnt -= 1
        return candidate
