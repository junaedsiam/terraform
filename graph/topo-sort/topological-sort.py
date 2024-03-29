"""
Problem description: 
---------
Given a Directed Acyclic Graph (DAG) with V vertices and E edges, Find any Topological Sorting of that Graph.

Example 1:

Input:

Output:
1
Explanation:
The output 1 denotes that the order is
valid. So, if you have, implemented
your function correctly, then output
would be 1 for all test cases.
One possible Topological order for the
graph is 3, 2, 1, 0.
Example 2:

Input:

Output:
1
Explanation:
The output 1 denotes that the order is
valid. So, if you have, implemented
your function correctly, then output
would be 1 for all test cases.
One possible Topological order for the
graph is 5, 4, 2, 1, 3, 0.
Your Task:
You don't need to read input or print anything. Your task is to complete the function topoSort()  which takes the integer V denoting the number of vertices and adjacency list as input parameters and returns an array consisting of the vertices in Topological order. As there are multiple Topological orders possible, you may return any of them. If your returned topo sort is correct then the console output will be 1 else 0.

Expected Time Complexity: O(V + E).
Expected Auxiliary Space: O(V).

Constraints:
2 ≤ V ≤ 104
1 ≤ E ≤ (N*(N-1))/2
"""
from queue import Queue


def dfs(node, adj, visited, stack):
    visited[node] = 1
    for adj_node in adj[node]:
        if not visited[adj_node]:
            dfs(adj_node, adj, visited, stack)
    stack.append(node)
# Function to return list containing vertices in Topological order.


def topological_sort_dfs(v, adj):
    # Code here

    visited = [0] * v
    stack = []

    for i in range(v):
        if not visited[i]:
            dfs(i, adj, visited, stack)

    return stack[::-1]


def topological_sort_bfs(v, adj):
    # Kahn's algorithm
    # indegrees of a vertex means how many edges are directed towards the vertex
    indegrees = [0] * v

    # Find indegrees
    for i in range(v):
        for node in adj[i]:
            indegrees[node] += 1

    q = Queue()

    # put item with 0 indegrees in the queue
    for i in range(v):
        if indegrees[i] == 0:
            q.put(i)

    res = []
    while q.qsize():
        node = q.get()
        # insert indegree 0 node in the result
        res.append(node)

        for adj_node in adj[node]:

            indegrees[adj_node] -= 1

            if indegrees[adj_node] == 0:
                q.put(adj_node)

    return res


if __name__ == '__main__':
    func = topological_sort_dfs
    print(func(4, [[], [0], [0], [0]]))
