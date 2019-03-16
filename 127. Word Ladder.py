class Solution:

    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        s_list = set(wordList)
        if endWord not in wordList:
            return 0
        ab = "abcdefghijklmnopqrstuvwxyz"
        q = collections.deque()
        q.append((beginWord, 1))
        s = set()
        while q:
            temp, level = q.popleft()
            if temp == endWord:
                return level
            for i in range(len(temp)):
                for a in ab:
                    new_temp = (temp[:i] + a + temp[i + 1:])
                    if new_temp in s_list and new_temp not in s:
                        q.append((new_temp, level + 1))
                        s.add(new_temp)
        return 0
