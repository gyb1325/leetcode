import heapq


class Solution:

    def getSkyline(self, buildings: List[List[int]]) -> List[List[int]]:
        events = [(L, -H, R) for L, R, H in buildings]
        temp = [(R, 0, 0) for _, R, _ in buildings]
        events = events + temp
        events.sort()
        res = [[0, 0]]
        live = [(0, float("inf"))]
        for L, negH, R in events:
            if negH:
                heapq.heappush(live, (negH, R))
            while live[0][1] <= L:
                heapq.heappop(live)
            if res[-1][1] != -live[0][0]:
                res.append([L, -live[0][0]])
        return res[1:]
