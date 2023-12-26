"""
Problem URL: https://leetcode.com/problems/network-delay-time/
---------

Problem Description:
---------
You are given a network of n nodes, labeled from 1 to n. You are also given times, a list of travel times as directed edges times[i] = (ui, vi, wi), where ui is the source node, vi is the target node, and wi is the time it takes for a signal to travel from source to target.

We will send a signal from a given node k. Return the minimum time it takes for all the n nodes to receive the signal. If it is impossible for all the n nodes to receive the signal, return -1.

 

Example 1:


Input: times = [[2,1,1],[2,3,1],[3,4,1]], n = 4, k = 2
Output: 2
Example 2:

Input: times = [[1,2,1]], n = 2, k = 1
Output: 1
Example 3:

Input: times = [[1,2,1]], n = 2, k = 2
Output: -1
 

Constraints:

1 <= k <= n <= 100
1 <= times.length <= 6000
times[i].length == 3
1 <= ui, vi <= n
ui != vi
0 <= wi <= 100
All the pairs (ui, vi) are unique. (i.e., no multiple edges.)

"""


from queue import Queue
from typing import List


def network_delay_time(times: List[List[int]], n: int, k: int) -> int:
    # create adjacent node
    adj = [[] for _ in range(n + 1)]
    sig_times = [float('inf')] * (n + 1)

    for u, v, w in times:
        adj[u].append((v, w))
    q = Queue()
    sig_times[k] = 0
    q.put(k)

    while q.qsize():
        node = q.get()

        for adj_node, weight in adj[node]:
            if sig_times[node] + weight < sig_times[adj_node]:
                sig_times[adj_node] = sig_times[node] + weight
                q.put(adj_node)

    res = float('-inf')

    for time in sig_times[1:]:
        if time == float('inf'):
            return -1
        res = max(res, time)

    return res


if __name__ == '__main__':
    print(network_delay_time([[2, 1, 1], [2, 3, 1], [3, 4, 1]], 4, 2))
