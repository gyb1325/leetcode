class Solution:

    def getHint(self, secret: str, guess: str) -> str:
        bull = 0
        cow = 0
        n = len(secret)
        dic_s = {}
        dic_g = {}
        for i in range(n):
            if secret[i] == guess[i]:
                bull += 1
            dic_s[secret[i]] = dic_s.get(secret[i], 0) + 1
            dic_g[guess[i]] = dic_g.get(guess[i], 0) + 1
        for key in dic_s:
            if key in dic_g:
                cow += min(dic_s[key], dic_g[key])
        cow -= bull
        return str(bull) + "A" + str(cow) + "B"
