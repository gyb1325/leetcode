class Solution:

    def findSubstring(self, s: str, words: List[str]) -> List[int]:
        dic = {}
        for w in words:
            dic[w] = dic.get(w, 0) + 1
        if not words:
            return []
        w_len = len(words[0])
        s_len = len(s)
        w_list_len = len(words)
        tot_len = w_list_len * w_len
        step = s_len - tot_len + 1
        if step < 0:
            return []
        cur_step = 0
        res = []
        while cur_step < step:

            break_flag = False
            temp = dic.copy()
            cur_s = s[cur_step:  cur_step + tot_len]
            for i in range(w_list_len):
                cur_word = cur_s[i * w_len: (i + 1) * w_len]
                if cur_word in temp:
                    temp[cur_word] -= 1
                    if temp[cur_word] < 0:
                        break_flag = True
                        break
                else:
                    break_flag = True
                    break
            if not break_flag:
                res.append(cur_step)
            cur_step += 1
        return res
