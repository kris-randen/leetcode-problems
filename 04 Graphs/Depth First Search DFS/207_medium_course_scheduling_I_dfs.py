"""

207. Course Schedule
Medium
13.9K
553
Companies
There are a total of numCourses courses you have to take, labeled from 0 to numCourses - 1. You are given an array prerequisites where prerequisites[i] = [ai, bi] indicates that you must take course bi first if you want to take course ai.

For example, the pair [0, 1], indicates that to take course 0 you have to first take course 1.
Return true if you can finish all courses. Otherwise, return false.



Example 1:

Input: numCourses = 2, prerequisites = [[1,0]]
Output: true
Explanation: There are a total of 2 courses to take.
To take course 1 you should have finished course 0. So it is possible.
Example 2:

Input: numCourses = 2, prerequisites = [[1,0],[0,1]]
Output: false
Explanation: There are a total of 2 courses to take.
To take course 1 you should have finished course 0, and to take course 0 you should also have finished course 1. So it is impossible.

"""

from collections import defaultdict

class Graph:
    def __init__(self, V, es):
        self.V = V
        self.adj = defaultdict(list)
        self.visited = [0] * V
        for e in es:
            self.add_edge(e[1], e[0])


    def add_edge(self, u, v):
        self.adj[u].append(v)

    def acyclic(self):
        def dfs(v):
            print(f'visited = {self.visited}')
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


if __name__ == '__main__':
    n = 2; ps = [[1, 0]]
    g = Graph(n, ps)
    print(g.acyclic())