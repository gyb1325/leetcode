class Solution:

    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = []
        nums.sort()
        N = len(nums)
        for i in range(N):
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            target = -nums[i]
            s = i + 1
            e = N - 1
            while s < e:
                if nums[s] + nums[e] == target:
                    res.append([nums[i], nums[s], nums[e]])
                    s += 1
                    while s < e and nums[s] == nums[s - 1]:
                        s += 1
                elif nums[s] + nums[e] < target:
                    s += 1
                else:
                    e -= 1
        return res
