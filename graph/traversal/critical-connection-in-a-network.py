"""
Problem URL: https://leetcode.com/problems/critical-connections-in-a-network/
---------

Problem Description:
---------

There are n servers numbered from 0 to n - 1 connected by undirected server-to-server connections forming a network where connections[i] = [ai, bi] represents a connection between servers ai and bi. Any server can reach other servers directly or indirectly through the network.

A critical connection is a connection that, if removed, will make some servers unable to reach some other server.

Return all critical connections in the network in any order.

 

Example 1:


Input: n = 4, connections = [[0,1],[1,2],[2,0],[1,3]]
Output: [[1,3]]
Explanation: [[3,1]] is also accepted.
Example 2:

Input: n = 2, connections = [[0,1]]
Output: [[0,1]]
 

Constraints:

2 <= n <= 105
n - 1 <= connections.length <= 105
0 <= ai, bi <= n - 1
ai != bi
There are no repeated connections.
"""


counter = 1


def dfs(adj, node, parent, vis, time, low, bridges):
    vis[node] = 1
    time[node] = low[node] = counter
    counter += 1

    for adj_node in adj[node]:

        if adj_node == parent:
            continue

        if not vis[adj_node]:
            dfs(adj, adj_node, node, vis, time, low, bridges)
            # set the low
            low[node] = min(low[node], low[adj_node])

            if low[adj_node] > time[node]:
                bridges.append((node, adj_node))
        else:
            low[node] = min(low[node], low[adj_node])


def critical_connection_in_a_network(n, connections):
    # Tarjan's Algorithm
    # make the adjacent list
    adj = [[] for _ in range(n)]

    for u, v in connections:
        adj[u].append(v)
        adj[v].append(u)
    # time of insertion, visited, low
    time = [0] * n
    visited = [0] * n
    low = [float('inf')] * n
    # bridges
    bridges = []
    # start the dfs
    dfs(adj, 0, -1, visited, time, low, bridges)

    return bridges


if __name__ == '__main__':
    print(critical_connection_in_a_network())
