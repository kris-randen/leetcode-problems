"""

210. Course Schedule II
Medium
9.5K
302
Companies
There are a total of numCourses courses you have to take, labeled from 0 to numCourses - 1. You are given an array prerequisites where prerequisites[i] = [ai, bi] indicates that you must take course bi first if you want to take course ai.

For example, the pair [0, 1], indicates that to take course 0 you have to first take course 1.
Return the ordering of courses you should take to finish all courses. If there are many valid answers, return any of them. If it is impossible to finish all courses, return an empty array.



Example 1:

Input: numCourses = 2, prerequisites = [[1,0]]
Output: [0,1]
Explanation: There are a total of 2 courses to take. To take course 1 you should have finished course 0. So the correct course order is [0,1].
Example 2:

Input: numCourses = 4, prerequisites = [[1,0],[2,0],[3,1],[3,2]]
Output: [0,2,1,3]
Explanation: There are a total of 4 courses to take. To take course 3 you should have finished both courses 1 and 2. Both courses 1 and 2 should be taken after you finished course 0.
So one correct course order is [0,1,2,3]. Another correct ordering is [0,2,1,3].
Example 3:

Input: numCourses = 1, prerequisites = []
Output: [0]

"""

from collections import defaultdict


class Graph:
    def __init__(self, V, edges):
        self.V = V
        self.adj = defaultdict(set)
        self.visited = [0] * V
        for edge in edges:
            self.add(edge[1], edge[0])

    def add(self, u, v):
        self.adj[u].add(v)

    def acyclic(self):
        def dfs(v):
            if self.visited[v] == 1: return True
            if self.visited[v] == -1: return False
            self.visited[v] = -1
            for w in self.adj[v]:
                if not dfs(w): return False
            self.visited[v] = 1
            return True

        for v in range(self.V):
            if not dfs(v): return False
        return True

    def sort(self):
        topological = []

        if not self.acyclic(): return topological

        def dfs(v):
            if self.visited[v] == 2: return
            self.visited[v] = 2
            for w in self.adj[v]:
                dfs(w)
            topological.append(v)

        for v in range(self.V):
            dfs(v)

        return reversed(topological)

