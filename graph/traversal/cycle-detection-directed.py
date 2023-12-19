"""
Problem description: 
---------
Given a directed graph with V vertices and E edges, check whether it contains any cycle or not. 


"""


def dfs(node, visited, path_visited, adj) -> bool:
    visited[node] = 1
    path_visited[node] = 1

    for adj_node in adj[node]:
        if not visited[adj_node]:
            # If the adj node is not visited and not in the path list
            dfs(adj_node, visited, path_visited, adj)

        # If adj node is visited and node is in the path:
        if path_visited[adj_node]:
            return True

    path_visited[node] = 0

    return False


def cycle_detection_directed(edges, v, e) -> bool:
    # visited: to track the visited vertices
    # path_visited: to track the visited path

    adj = [[] for _ in range(v)]
    visited = [0] * v
    path_visited = [0] * v
    # First create an adjacency list from edges
    for edge in edges:
        adj[edge[0]].append(edge[1])

    for i in range(v):
        if not visited[i]:
            if dfs(i, visited, path_visited, adj):
                return True

    return False


if __name__ == '__main__':
    print(cycle_detection_directed([[0, 1], [
        1, 2], [
        2, 3],
        [3, 0]], 4, 4))
