# O(nlog(n))
# class Solution:
#     def hIndex(self, citations: List[int]) -> int:
#         citations.sort()
#         n = len(citations)
#         for i in range(n):
#             if citations[i] >= n-i:
#                 return n-i
#         return 0

# O(n)


class Solution:

    def hIndex(self, citations: List[int]) -> int:
        n = len(citations)
        bucket = [0] * (n + 1)
        for cit in citations:
            if cit >= n:
                bucket[n] += 1
            else:
                bucket[cit] += 1
        cnt = 0
        for i in range(n, -1, -1):
            cnt += bucket[i]
            if cnt >= i:
                return i
        return 0
