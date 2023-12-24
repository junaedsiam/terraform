"""
Problem description: 
---------

"""
from typing import List
from queue import Queue


def shortest_path_in_a_dag(n: int, m: int, edges: List[List[int]]) -> List[int]:
    # [u, v, weight]
    adj = [[] for _ in range(n)]

    for i in range(m):
        u, v, weight = edges[i]
        adj[u].append((v, weight))

    res = [float('inf')] * n
    q = Queue()
    q.put((0))
    res[0] = 0

    while q.qsize():
        node = q.get()

        for adj_node, weight in adj[node]:
            if res[node] + weight < res[adj_node]:
                res[adj_node] = res[node] + weight
                q.put(adj_node)

    return [val if val != float('inf') else -1 for val in res]


if __name__ == '__main__':
    print(shortest_path_in_a_dag(6, 7, [[0, 1, 2], [0, 4, 1], [
          4, 5, 4], [4, 2, 2], [1, 2, 3], [2, 3, 6], [5, 3, 1]]))
