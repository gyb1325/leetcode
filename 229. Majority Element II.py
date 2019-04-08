class Solution:

    def majorityElement(self, nums: List[int]) -> List[int]:
        if not nums:
            return []
        if len(nums) <= 2:
            return list(set(nums))
        cnt1, cnt2, candidate1, candidate2 = 0, 0, 0, 1
        for n in nums:
            if candidate1 == n:
                cnt1 += 1
            elif candidate2 == n:
                cnt2 += 1
            elif cnt1 == 0:
                candidate1, cnt1 = n, 1
            elif cnt2 == 0:
                candidate2, cnt2 = n, 1
            else:
                cnt1 -= 1
                cnt2 -= 1
        lst = [candidate1, candidate2]

        return [i for i in lst if nums.count(i) > len(nums) // 3]
