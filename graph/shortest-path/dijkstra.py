"""
Problem description: 
---------

"""


def dijkstra(V, adj, S):
    # code here
    s = set()
    dist = [float('inf')] * V
    s.add(S)
    dist[S] = 0

    while len(s):
        node = s.pop()

        for edge in adj[node]:
            adj_node = edge[0]
            weight = edge[1]
            if dist[node] + weight < dist[adj_node]:
                dist[adj_node] = dist[node] + weight
                s.add(adj_node)

    return dist


if __name__ == '__main__':
    print(dijkstra(2, [[[1, 9]], [[0, 9]]], 0))
