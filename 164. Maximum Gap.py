class Solution:

    def maximumGap(self, nums: List[int]) -> int:
        n = len(nums)
        if n <= 1:
            return 0
        min_val = min(nums)
        max_val = max(nums)
        gap = math.ceil((float)(max_val - min_val) / (n - 1))

        bucket_min = [float("inf")] * (n - 1)
        bucket_max = [float("-inf")] * (n - 1)

        for num in nums:
            if num == min_val or num == max_val:
                continue
            idx = (num - min_val) // gap
            bucket_min[idx] = min(bucket_min[idx], num)
            bucket_max[idx] = max(bucket_max[idx], num)
        print(bucket_min, bucket_max)
        prev = min_val
        max_gap = 0
        for i in range(n - 1):
            if bucket_min[i] == float("inf") or bucket_max[i] == float("-inf"):
                continue
            max_gap = max(max_gap, bucket_min[i] - prev)
            prev = bucket_max[i]
        max_gap = max(max_gap, max_val - prev)

        return max_gap
