class Solution:

    def containsNearbyAlmostDuplicate(self, nums: List[int], k: int, t: int) -> bool:
        bucket = {}
        for i, v in enumerate(nums):
            bucknum, offset = (v // t, 1) if t else (v, 0)
            for idx in range(bucknum - offset, bucknum + offset + 1):
                if idx in bucket and abs(bucket[idx] - nums[i]) <= t:
                    return True
            bucket[bucknum] = nums[i]
            if len(bucket) > k:
                del bucket[nums[i - k] // t if t else nums[i - k]]
        return False
