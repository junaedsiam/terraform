"""
Problem description: 
---------
Given a sorted dictionary of an alien language having N words and k starting alphabets of standard dictionary. Find the order of characters in the alien language.
Note: Many orders may be possible for a particular test case, thus you may return any valid order and output will be 1 if the order of string returned by the function is correct else 0 denoting incorrect string returned.
 

Example 1:

Input: 
N = 5, K = 4
dict = {"baa","abcd","abca","cab","cad"}
Output:
1
Explanation:
Here order of characters is 
'b', 'd', 'a', 'c' Note that words are sorted 
and in the given language "baa" comes before 
"abcd", therefore 'b' is before 'a' in output.
Similarly we can find other orders.
Example 2:

Input: 
N = 3, K = 3
dict = {"caa","aaa","aab"}
Output:
1
Explanation:
Here order of characters is
'c', 'a', 'b' Note that words are sorted
and in the given language "caa" comes before
"aaa", therefore 'c' is before 'a' in output.
Similarly we can find other orders.
 

Your Task:
You don't need to read or print anything. Your task is to complete the function findOrder() which takes  the string array dict[], its size N and the integer K as input parameter and returns a string denoting the order of characters in the alien language.


Expected Time Complexity: O(N * |S| + K) , where |S| denotes maximum length.
Expected Space Compelxity: O(K)


Constraints:
1 ≤ N, M ≤ 300
1 ≤ K ≤ 26
1 ≤ Length of words ≤ 50


"""
from queue import Queue


def setAdj(pos, alien_dict, adj):
    first = alien_dict[pos]
    sec = alien_dict[pos + 1]

    ln = min(len(first), len(sec))

    for i in range(ln):
        if first[i] != sec[i]:
            adj[ord(first[i]) - ord('a')].append(ord(sec[i]) - ord('a'))
            break


def topoSort(k, adj):
    # find indegrees from adj list
    indegrees = [0] * k
    res = []
    for i in range(k):
        for adj_node in adj[i]:
            indegrees[adj_node] += 1
    # if indegrees zero for any node insert them in the queue first
    q = Queue()

    for i in range(k):
        if indegrees[i] == 0:
            q.put(i)

    # go through the queue
    while q.qsize():
        node = q.get()
        res.append(node)
        for adj_node in adj[node]:
            indegrees[adj_node] -= 1
            if indegrees[adj_node] == 0:
                q.put(adj_node)

    return res


def alien_dictionaries(alien_dict, N, K):
    # Have to create the adjacency list from the alien dict
    adj = [[] for _ in range(K)]

    for i in range(N - 1):
        setAdj(i, alien_dict, adj)

    res = topoSort(K, adj)
    return "".join(map(lambda x: chr(ord('a') + x), res))


if __name__ == '__main__':
    print(alien_dictionaries(['baa', 'abcd', 'abca', 'cab', 'cada'], 5, 4))
