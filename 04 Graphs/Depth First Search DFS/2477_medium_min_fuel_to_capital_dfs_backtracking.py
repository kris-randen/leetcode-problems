"""

2477. Minimum Fuel Cost to Report to the Capital
Medium
1.9K
74
Companies
There is a tree (i.e., a connected, undirected graph with no cycles) structure country network consisting of n cities numbered from 0 to n - 1 and exactly n - 1 roads. The capital city is city 0. You are given a 2D integer array roads where roads[i] = [ai, bi] denotes that there exists a bidirectional road connecting cities ai and bi.

There is a meeting for the representatives of each city. The meeting is in the capital city.

There is a car in each city. You are given an integer seats that indicates the number of seats in each car.

A representative can use the car in their city to travel or change the car and ride with another representative. The cost of traveling between two cities is one liter of fuel.

Return the minimum number of liters of fuel to reach the capital city.



Example 1:


Input: roads = [[0,1],[0,2],[0,3]], seats = 5
Output: 3
Explanation:
- Representative1 goes directly to the capital with 1 liter of fuel.
- Representative2 goes directly to the capital with 1 liter of fuel.
- Representative3 goes directly to the capital with 1 liter of fuel.
It costs 3 liters of fuel at minimum.
It can be proven that 3 is the minimum number of liters of fuel needed.
Example 2:


Input: roads = [[3,1],[3,2],[1,0],[0,4],[0,5],[4,6]], seats = 2
Output: 7
Explanation:
- Representative2 goes directly to city 3 with 1 liter of fuel.
- Representative2 and representative3 go together to city 1 with 1 liter of fuel.
- Representative2 and representative3 go together to the capital with 1 liter of fuel.
- Representative1 goes directly to the capital with 1 liter of fuel.
- Representative5 goes directly to the capital with 1 liter of fuel.
- Representative6 goes directly to city 4 with 1 liter of fuel.
- Representative4 and representative6 go together to the capital with 1 liter of fuel.
It costs 7 liters of fuel at minimum.
It can be proven that 7 is the minimum number of liters of fuel needed.
Example 3:


Input: roads = [], seats = 1
Output: 0
Explanation: No representatives need to travel to the capital city.

"""
import math
from collections import defaultdict
from typing import List

class Graph:
    def __init__(self, V, es=None, di=True):
        self.V, self.es = V, es if es else []
        self.di, self.adj = di, defaultdict(set)
        for u, v in es: self.add(u, v)

    def add(self, u, v):
        self.adj[u].add(v)
        if not self.di: self.adj[v].add(u)


class DFS:
    def __init__(self, g):
        self.g = g; self.visited = [0] * self.g.V

    def min_cost(self, cap):
        cost, s = 0, 0

        def dfs(u):
            nonlocal cost
            if len(self.g.adj[u]) == 1 and u != s:
                return 1, 1
            self.visited[u] = 1
            cars, men = 0, 1
            for v in self.g.adj[u]:
                if self.visited[v]: continue
                c, m = dfs(v)
                men += m; cost += c
            cars = math.ceil(men / cap)
            return cars, men

        dfs(s); return cost


# class Solution:
#     def minimumFuelCost(self, roads: List[List[int]], seats: int) -> int:
#         V = len(roads) + 1; g = Graph(V, roads, di=False); dfs = DFS(g)
#         return dfs.min_cost(seats)


class Solution:
    def minimumFuelCost(self, roads: List[List[int]], seats: int) -> int:
        g, visited, cost = defaultdict(list), set(), 0
        for s, t in roads: g[s].append(t); g[t].append(s)

        def dfs(u):
            nonlocal cost
            if len(g[u]) == 1 and u != 0: return 1, 1
            visited.add(u)
            cars, men = 0, 1
            for v in g[u]:
                if v in visited: continue
                c, m = dfs(v)
                men += m; cost += c
            cars = math.ceil(men / seats)
            return cars, men

        dfs(0); return cost