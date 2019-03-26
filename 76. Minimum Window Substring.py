class Solution:

    def minWindow(self, s: str, t: str) -> str:
        dic = {}
        for c in t:
            dic[c] = dic.get(c, 0) + 1
        start, end, head = 0, 0, 0
        min_len = len(s) + 1
        cnt = len(t)
        while end < len(s):
            if s[end] in dic:
                if dic[s[end]] > 0:
                    cnt -= 1
                dic[s[end]] -= 1
            end += 1

            while cnt == 0:
                if end - start < min_len:
                    head = start
                    min_len = end - start
                if s[start] in dic:
                    dic[s[start]] += 1
                    if dic[s[start]] > 0:
                        cnt += 1
                start += 1
        return s[head: head + min_len] if min_len < len(s) + 1 else ""
