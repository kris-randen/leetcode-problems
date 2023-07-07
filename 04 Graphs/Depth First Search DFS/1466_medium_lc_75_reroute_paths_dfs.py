"""

1466. Reorder Routes to Make All Paths Lead to the City Zero
Medium
3.5K
78
Companies
There are n cities numbered from 0 to n - 1 and n - 1 roads such that there is only one way to travel between two different cities (this network form a tree). Last year, The ministry of transport decided to orient the roads in one direction because they are too narrow.

Roads are represented by connections where connections[i] = [ai, bi] represents a road from city ai to city bi.

This year, there will be a big event in the capital (city 0), and many people want to travel to this city.

Your task consists of reorienting some roads such that each city can visit the city 0. Return the minimum number of edges changed.

It's guaranteed that each city can reach city 0 after reorder.



Example 1:


Input: n = 6, connections = [[0,1],[1,3],[2,3],[4,0],[4,5]]
Output: 3
Explanation: Change the direction of edges show in red such that each node can reach the node 0 (capital).
Example 2:


Input: n = 5, connections = [[1,0],[1,2],[3,2],[3,4]]
Output: 2
Explanation: Change the direction of edges show in red such that each node can reach the node 0 (capital).
Example 3:

Input: n = 3, connections = [[1,0],[2,0]]
Output: 0

"""

"""

Python Depth-First Search (DFS) Solution
kris-randen
237
2
18 minutes ago
Python3
Intuition
Depth-First Search (DFS)

Approach
You start from the sink aka 0 and travel outwards irrespective of what direction the edge is pointing in. We have to make sure we invert the ones that are pointing away from 0 i.e., in the direction of DFS.

Complexity
Time complexity:
O(n)

Space complexity:
O(n)

"""

from collections import defaultdict

def graph(roads):
    adj = defaultdict(set)
    for (s, e) in roads:
        adj[s + 1].add(e + 1); adj[e + 1].add(-s - 1)
    return adj

def graph_a(roads):
    adj = []

def min_reorder(roads):
    adj, visited, count = graph(roads), set(), 0

    def dfs(i):
        nonlocal count
        if i in visited: return
        visited.add(i)
        for j in adj[i]:
            if -i in adj[abs(j)] and abs(j) not in visited: count += 1
            dfs(abs(j))

    dfs(1)

    return count