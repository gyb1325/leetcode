class Solution:

    def combine(self, n: int, k: int) -> List[List[int]]:
        res = []
        lst = [i for i in range(1, n + 1)]
        self.helper(lst, k, [], res)
        return res

    def helper(self, lst, k, path, res):
        if k == 0:
            res.append(path)
        if lst:
            for i in range(len(lst)):
                self.helper(lst[i + 1:], k - 1, path + [lst[i]], res)
