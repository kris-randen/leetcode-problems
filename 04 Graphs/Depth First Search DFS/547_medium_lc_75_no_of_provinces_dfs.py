"""

547. Number of Provinces
Medium
8.5K
317
Companies
There are n cities. Some of them are connected, while some are not. If city a is connected directly with city b, and city b is connected directly with city c, then city a is connected indirectly with city c.

A province is a group of directly or indirectly connected cities and no other cities outside of the group.

You are given an n x n matrix isConnected where isConnected[i][j] = 1 if the ith city and the jth city are directly connected, and isConnected[i][j] = 0 otherwise.

Return the total number of provinces.



Example 1:


Input: isConnected = [[1,1,0],[1,1,0],[0,0,1]]
Output: 2
Example 2:


Input: isConnected = [[1,0,0],[0,1,0],[0,0,1]]
Output: 3

"""

def provinces(cities):
    n, count, visited = len(cities), 0, set()

    def dfs(i):
        if i in visited: return
        visited.add(i)
        for city in cities[i]:
            dfs(city)

    for city in cities:
        if city not in visited:
            dfs(city); count += 1

    return count
