"""
Problem URL: https://leetcode.com/problems/find-the-city-with-the-smallest-number-of-neighbors-at-a-threshold-distance/description/
---------

Problem Description:
---------

There are n cities numbered from 0 to n-1. Given the array edges where edges[i] = [fromi, toi, weighti] represents a bidirectional and weighted edge between cities fromi and toi, and given the integer distanceThreshold.

Return the city with the smallest number of cities that are reachable through some path and whose distance is at most distanceThreshold, If there are multiple such cities, return the city with the greatest number.

Notice that the distance of a path connecting cities i and j is equal to the sum of the edges' weights along that path.

 

Example 1:


Input: n = 4, edges = [[0,1,3],[1,2,1],[1,3,4],[2,3,1]], distanceThreshold = 4
Output: 3
Explanation: The figure above describes the graph. 
The neighboring cities at a distanceThreshold = 4 for each city are:
City 0 -> [City 1, City 2] 
City 1 -> [City 0, City 2, City 3] 
City 2 -> [City 0, City 1, City 3] 
City 3 -> [City 1, City 2] 
Cities 0 and 3 have 2 neighboring cities at a distanceThreshold = 4, but we have to return city 3 since it has the greatest number.
Example 2:


Input: n = 5, edges = [[0,1,2],[0,4,8],[1,2,3],[1,4,2],[2,3,1],[3,4,1]], distanceThreshold = 2
Output: 0
Explanation: The figure above describes the graph. 
The neighboring cities at a distanceThreshold = 2 for each city are:
City 0 -> [City 1] 
City 1 -> [City 0, City 4] 
City 2 -> [City 3, City 4] 
City 3 -> [City 2, City 4]
City 4 -> [City 1, City 2, City 3] 
The city 0 has 1 neighboring city at a distanceThreshold = 2.
 

Constraints:

2 <= n <= 100
1 <= edges.length <= n * (n - 1) / 2
edges[i].length == 3
0 <= fromi < toi < n
1 <= weighti, distanceThreshold <= 10^4
All pairs (fromi, toi) are distinct.
"""


from typing import List


def find_the_city_with_smallest_number_of_neighbors(n: int, edges: List[List[int]], distanceThreshold: int) -> int:
    """
    From the problem description, we can see that we need to do the 
    followings
    1. we have to find shortest distance from all pairs to all pairs
    2. Then in a seperate traversal we can find the city with the
    smallest number of reachable cities

    To achive 1, we can do either one of the following- 
    1. We can use dijkstra. In that case we have to take each vertex,
    and perform dijkstra on that vertex as a source, and other vertices as destinations
    2. Or we can apply floyd warshall algorithm to achieve it in one go
    For this solution lets use floyd warshall
    """
    dist = [[float('inf')] * n for _ in range(n)]

    # setting same vertex distance 0
    for i in range(n):
        for j in range(n):
            if i == j:
                dist[i][j] = 0

    for u, v, w in edges:
        # As it is bidirectional
        dist[u][v] = w
        dist[v][u] = w

    # via
    for v in range(n):
        # from
        for i in range(n):
            # to
            for j in range(n):
                new_val = dist[i][v] + dist[v][j]
                if new_val < dist[i][j]:
                    dist[i][j] = new_val

    # finding cities with smallest number of reachable cities
    min_count = float('inf')
    vertex = float('-inf')

    for i in range(n):
        count = 0
        for j in range(n):
            if dist[i][j] != float('inf') and dist[i][j] <= distanceThreshold:
                count += 1
        if count < min_count:
            min_count = count
            vertex = i
        elif count == min_count:
            vertex = max(vertex, i)

    return vertex


if __name__ == '__main__':
    print(find_the_city_with_smallest_number_of_neighbors(4,
                                                          [[0, 1, 3], [1, 2, 1], [1, 3, 4], [2, 3, 1]], 4))
