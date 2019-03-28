# BFS
class Solution:

    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        graph = [[] for i in range(numCourses)]
        in_degree = [0] * numCourses
        for i, j in prerequisites:
            graph[j].append(i)
            in_degree[i] += 1

        bfs = [i for i in range(numCourses) if in_degree[i] == 0]

        for c in bfs:
            for node in graph[c]:
                in_degree[node] -= 1
                if in_degree[node] == 0:
                    bfs.append(node)
        return len(bfs) == numCourses


# DFS
class Solution:

    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        self.graph = [[] for _ in range(numCourses)]
        self.visit = [0] * numCourses
        for x, y in prerequisites:
            self.graph[x].append(y)
        for i in range(numCourses):
            if not self.dfs(i):
                return False
        return True

    def dfs(self, i):
        if self.visit[i] == -1:
            return False
        if self.visit[i] == 1:
            return True
        self.visit[i] = -1
        for j in self.graph[i]:
            if not self.dfs(j):
                return False
        self.visit[i] = 1
        return True
