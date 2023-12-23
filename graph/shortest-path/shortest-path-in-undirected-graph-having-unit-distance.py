"""
Problem description: 
---------

"""
from queue import Queue


def shortest_path_in_undirected_graph_having_unit_distance(edges, n, m, src):
    # code here
    # Create adj node first
    # Do BFS to find the distance for each node
    adj = [[] for _ in range(n)]
    distances = [float('inf') for _ in range(n)]

    for i in range(m):
        u, v = edges[i]
        adj[u].append(v)
        adj[v].append(u)

    q = Queue()
    q.put(src)
    distances[src] = 0

    while q.qsize():
        node = q.get()

        for anode in adj[node]:
            if distances[node] + 1 < distances[anode]:
                distances[anode] = distances[node] + 1
                q.put(anode)

    return [-1 if val == float('inf') else val for val in distances]


if __name__ == '__main__':
    print(shortest_path_in_undirected_graph_having_unit_distance([[0, 1], [0, 3], [
          3, 4], [4, 5], [5, 6], [1, 2], [2, 6], [6, 7], [7, 8], [6, 8]], 9, 10, 0))
