class Solution:

    def threeSumClosest(self, nums: List[int], target: int) -> int:
        nums.sort()
        N = len(nums)
        closest = (float("inf"), 0)
        for i in range(N):
            new_target = target - nums[i]
            s = i + 1
            e = N - 1
            while s < e:
                diff = new_target - nums[s] - nums[e]
                if diff == 0:
                    return target
                abs_diff = abs(diff)
                if abs_diff < closest[0]:
                    closest = (abs_diff, nums[i] + nums[s] + nums[e])
                if diff > 0:
                    s += 1
                else:
                    e -= 1
        return closest[1]
