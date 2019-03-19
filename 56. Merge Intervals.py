# Definition for an interval.
# class Interval:
#     def __init__(self, s=0, e=0):
#         self.start = s
#         self.end = e


class Solution:

    def merge(self, intervals: List[Interval]) -> List[Interval]:
        n = len(intervals)
        if n <= 1:
            return intervals
        intervals.sort(key=lambda x: x.start)
        res = [intervals[0]]
        for i in range(1, n):
            if intervals[i].start <= res[-1].end:
                res[-1].end = max(intervals[i].end, res[-1].end)
            else:
                res.append(intervals[i])
        return res
