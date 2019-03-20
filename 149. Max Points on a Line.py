# Definition for a point.
# class Point:
#     def __init__(self, a=0, b=0):
#         self.x = a
#         self.y = b
import decimal


class Solution:

    def maxPoints(self, points: List[Point]) -> int:
        n = len(points)
        if n == 1:
            return 1
        res = 0
        for i in range(n - 1):
            same_point = 1
            dic = {}
            local_max = 0
            for j in range(i + 1, n):
                if points[i].x == points[j].x and points[i].y == points[j].y:
                    same_point += 1
                elif points[i].x == points[j].x:
                    dic["MAX"] = dic.get("MAX", 0) + 1
                    if dic["MAX"] > local_max:
                        local_max = dic["MAX"]
                else:
                    slope0 = decimal.Decimal(points[i].y - points[j].y) / decimal.Decimal(points[i].x - points[j].x)
                    slope1 = decimal.Decimal((points[i].y - points[j].y) / (points[i].x - points[j].x))
                    dic[(slope0, slope1)] = dic.get((slope0, slope1), 0) + 1
                    if dic[(slope0, slope1)] > local_max:
                        local_max = dic[(slope0, slope1)]
            local_max += same_point
            res = max(local_max, res)

        return res
