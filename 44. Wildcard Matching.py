class Solution:

    def isMatch(self, s: str, p: str) -> bool:
        m = len(s)
        n = len(p)
        aux = [[False] * (n + 1) for _ in range(m + 1)]

        for i in range(m + 1):
            for j in range(n + 1):
                if i == 0 and j == 0:
                    aux[i][j] = True
                elif i == 0:
                    if p[j - 1] == "*":
                        aux[i][j] = aux[i][j - 1]
                    else:
                        aux[i][j] = False
                elif j == 0:
                    aux[i][j] = False
                else:
                    aux[i][j] = (aux[i - 1][j - 1] and (s[i - 1] == p[j - 1] or p[j - 1] == "*" or p[j - 1] == "?")) \
                        or (aux[i - 1][j] and p[j - 1] == "*") or (aux[i][j - 1] and p[j - 1] == "*")
        return aux[-1][-1]
