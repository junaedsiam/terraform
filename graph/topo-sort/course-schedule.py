"""
Problem description: 
---------
There are a total of numCourses courses you have to take, labeled from 0 to numCourses - 1. You are given an array prerequisites where prerequisites[i] = [ai, bi] indicates that you must take course bi first if you want to take course ai.

For example, the pair [0, 1], indicates that to take course 0 you have to first take course 1.
Return the ordering of courses you should take to finish all courses. If there are many valid answers, return any of them. If it is impossible to finish all courses, return an empty array.

 

Example 1:

Input: numCourses = 2, prerequisites = [[1,0]]
Output: [0,1]
Explanation: There are a total of 2 courses to take. To take course 1 you should have finished course 0. So the correct course order is [0,1].
Example 2:

Input: numCourses = 4, prerequisites = [[1,0],[2,0],[3,1],[3,2]]
Output: [0,2,1,3]
Explanation: There are a total of 4 courses to take. To take course 3 you should have finished both courses 1 and 2. Both courses 1 and 2 should be taken after you finished course 0.
So one correct course order is [0,1,2,3]. Another correct ordering is [0,2,1,3].
Example 3:

Input: numCourses = 1, prerequisites = []
Output: [0]
 

Constraints:

1 <= numCourses <= 2000
0 <= prerequisites.length <= numCourses * (numCourses - 1)
prerequisites[i].length == 2
0 <= ai, bi < numCourses
ai != bi
All the pairs [ai, bi] are distinct.
"""
from queue import Queue


def topological_sort(adj, v):
    q = Queue()
    indegrees = [0] * v

    for i in range(v):
        for node in adj[i]:
            indegrees[node] += 1

    for i in range(v):
        if indegrees[i] == 0:
            q.put(i)

    res = []
    while q.qsize():
        node = q.get()
        res.append(node)
        for adj_node in adj[node]:
            indegrees[adj_node] -= 1
            if indegrees[adj_node] == 0:
                q.put(adj_node)

    return res


def course_schedule(numCourses, prerequisites):
    adj = [[] for _ in range(numCourses)]

    for course, pre in prerequisites:
        adj[pre].append(course)

    res = topological_sort(adj, numCourses)

    return res if len(res) == numCourses else []


if __name__ == '__main__':
    print(course_schedule(4, [[1, 0], [2, 0], [3, 1], [3, 2]]))
