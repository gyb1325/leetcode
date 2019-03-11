class Solution:

    def longestCommonPrefix(self, strs: List[str]) -> str:
        if not strs:
            return ""
        steps = len(strs[0])
        t_flag = False
        prefix = ""
        for i in range(steps):
            for j in range(1, len(strs)):
                if len(strs[j]) > i:
                    if strs[j][i] != strs[0][i]:
                        t_flag = True
                        break
                else:
                    t_flag = True
                    break
            if t_flag:
                break
            else:
                prefix = prefix + strs[0][i]

        return prefix
