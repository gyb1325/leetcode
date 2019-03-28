class Solution:

    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        graph = [[] for _ in range(numCourses)]
        inDegree = [0] * numCourses
        for i, j in prerequisites:
            graph[j].append(i)
            inDegree[i] += 1

        bfs = [i for i in range(numCourses) if inDegree[i] == 0]

        for i in bfs:
            for node in graph[i]:
                inDegree[node] -= 1
                if inDegree[node] == 0:
                    bfs.append(node)
        return bfs if len(bfs) == numCourses else []
