"""

1462. Course Schedule IV
Medium
1.2K
55
Companies
There are a total of numCourses courses you have to take, labeled from 0 to numCourses - 1. You are given an array prerequisites where prerequisites[i] = [ai, bi] indicates that you must take course ai first if you want to take course bi.

For example, the pair [0, 1] indicates that you have to take course 0 before you can take course 1.
Prerequisites can also be indirect. If course a is a prerequisite of course b, and course b is a prerequisite of course c, then course a is a prerequisite of course c.

You are also given an array queries where queries[j] = [uj, vj]. For the jth query, you should answer whether course uj is a prerequisite of course vj or not.

Return a boolean array answer, where answer[j] is the answer to the jth query.



Example 1:


Input: numCourses = 2, prerequisites = [[1,0]], queries = [[0,1],[1,0]]
Output: [false,true]
Explanation: The pair [1, 0] indicates that you have to take course 1 before you can take course 0.
Course 0 is not a prerequisite of course 1, but the opposite is true.
Example 2:

Input: numCourses = 2, prerequisites = [], queries = [[1,0],[0,1]]
Output: [false,false]
Explanation: There are no prerequisites, and each course is independent.
Example 3:


Input: numCourses = 3, prerequisites = [[1,2],[1,0],[2,0]], queries = [[1,0],[1,2]]
Output: [true,true]

"""

from collections import defaultdict
from collections import deque

class Graph:
    def __init__(self, V, es):
        self.V = V
        self.adj = defaultdict(set)
        self.visited = [0] * V
        for e in es:
            self.add(e[0], e[1])
        self.rewire()

    def add(self, u, v):
        self.adj[u].add(v)

    def clear_visited(self):
        self.visited = [0] * self.V

    def sort(self):
        topological = deque()

        def dfs(v):
            if self.visited[v]: return
            self.visited[v] = 1
            for w in self.adj[v]:
                dfs(w)
            topological.appendleft(v)

        for v in range(self.V):
            dfs(v)

        self.clear_visited()
        return topological

    def rewire(self):
        seq = self.sort()
        print(f'rewire seq = {seq}')

        def dfs_wire(v, heads):
            if self.visited[v]: return
            self.visited[v] = 1
            for w in self.adj[v].copy():
                dfs_wire(w, heads + [v])
            for head in heads:
                self.add(head, v)

        while seq:
            p = seq.popleft()
            print(f'seq looping p = {p}')
            dfs_wire(p, [])


    def query(self, q):
        return q[1] in self.adj[q[0]]

    def queries(self, qs):
        return list(map(lambda q: self.query(q), qs))

if __name__ == '__main__':
    n = 5
    ps = [[4, 3], [4, 1], [4, 0], [3, 2], [3, 1], [3, 0], [2, 1], [1, 0]]
    qs = [[1, 4], [4, 2], [0, 1], [4, 0], [0, 2], [1, 3], [0, 1]]
    g = Graph(n, ps)
    print(g.queries(qs))
