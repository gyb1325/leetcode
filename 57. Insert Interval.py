# Definition for an interval.
# class Interval:
#     def __init__(self, s=0, e=0):
#         self.start = s
#         self.end = e


class Solution:

    def insert(self, intervals: List[Interval], newInterval: Interval) -> List[Interval]:
        intervals.append(newInterval)
        intervals.sort(key=lambda x: x.start)

        res = [intervals[0]]
        for i in intervals[1:]:
            if res[-1].end >= i.start:
                res[-1].end = max(res[-1].end, i.end)
            else:
                res.append(i)
        return res
