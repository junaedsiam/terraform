"""
Problem description: 
---------
Given an undirected graph with V vertices and E edges, check whether it contains any cycle or not. Graph is in the form of adjacency list where adj[i] contains all the nodes ith node is having edge with.

Example 1:

Input:  
V = 5, E = 5
adj = {{1}, {0, 2, 4}, {1, 3}, {2, 4}, {1, 3}} 
Output: 1
Explanation: 

1->2->3->4->1 is a cycle.
Example 2:

Input: 
V = 4, E = 2
adj = {{}, {2}, {1, 3}, {2}}
Output: 0
Explanation: 

No cycle in the graph.
 

Your Task:
You don't need to read or print anything. Your task is to complete the function isCycle() which takes V denoting the number of vertices and adjacency list as input parameters and returns a boolean value denoting if the undirected graph contains any cycle or not, return 1 if a cycle is present else return 0.

NOTE: The adjacency list denotes the edges of the graph where edges[i] stores all other vertices to which ith vertex is connected.

 

Expected Time Complexity: O(V + E)
Expected Space Complexity: O(V)


 

Constraints:
1 ≤ V, E ≤ 105


"""
from queue import Queue


def bfs(src, visited, adj):
    q = Queue()
    q.put((src, -1))

    while q.qsize():
        node, parent = q.get()
        for adj_node in adj[node]:
            if not visited[adj_node]:
                visited[adj_node] = 1
                q.put((adj_node, node))

            elif adj_node != parent:
                return True

    return False


def cycle_detection(vertices, adj):
    visited = [0] * vertices

    for i in range(vertices):
        if not visited[i]:
            if bfs(i, visited, adj):
                return True
    return False


if __name__ == '__main__':
    print(cycle_detection(5, [[1], [0, 2, 4], [1, 3], [2, 4], [1, 3]]))
    print(cycle_detection(4, [[], [2], [1, 3], [2]]))
