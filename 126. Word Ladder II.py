# Time Limited Exceeded Answer
# class Solution:

#     def findLadders(self, beginWord: str, endWord: str, wordList: List[str]) -> List[List[str]]:
#         s_list = set(wordList)
#         if endWord not in wordList:
#             return []
#         res = []
#         s = set()
#         self.helper(beginWord, endWord, s_list, s, [beginWord], res)
#         return res

#     def helper(self, temp, endWord, s_list, s, path, res):
#         if res and len(res[0]) < len(path):
#             return
#         if temp == endWord:
#             if not res:
#                 res.append(path)
#             else:
#                 if len(res[0]) == len(path):
#                     res.append(path)
#                 elif len(res[0]) < len(path):
#                     return
#                 else:
#                     res.clear()
#                     res.append(path)

#         ab = "abcdefghijklmnopqrstuvwxyz"
#         for i in range(len(temp)):
#             for a in ab:
#                 new_temp = (temp[:i] + a + temp[i + 1:])
#                 if new_temp in s_list and new_temp not in s:
#                     s.add(new_temp)
#                     self.helper(new_temp, endWord, s_list, s, path + [new_temp], res)
#                     s.remove(new_temp)


class Solution:

    def findLadders(self, beginWord: str, endWord: str, wordList: List[str]) -> List[List[str]]:
        layer = {beginWord: [[beginWord]]}
        wordList = set(wordList)
        res = []
        while layer:
            new_layer = collections.defaultdict(list)
            for w in layer:
                if w == endWord:
                    res.extend(k for k in layer[w])
                else:
                    for i in range(len(w)):
                        for c in "abcdefghijklmnopqrstuvwxyz":
                            new_temp = w[:i] + c + w[i + 1:]
                            if new_temp in wordList:
                                new_layer[new_temp] += [j + [new_temp] for j in layer[w]]
            wordList -= set(new_layer.keys())
            layer = new_layer
        return res
