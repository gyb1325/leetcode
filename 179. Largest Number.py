from functools import cmp_to_key


class Solution:

    def largestNumber(self, nums: List[int]) -> str:
        def cmp(a, b):
            return int(b + a) - int(a + b)

        nums = list(map(str, nums))
        nums.sort(key=cmp_to_key(cmp))
        return "".join(nums).lstrip("0") or "0"
