"""
Theory URL: https://takeuforward.org/data-structure/disjoint-set-union-by-rank-union-by-size-path-compression-g-46/ 
---------


"""


class DisjointSet:
    def __init__(self, n):
        self.rank = [0] * (n + 1)
        self.size = [1] * (n + 1)
        self.parent = [i for i in range(n + 1)]

    def findUltimateParent(self, node):
        if node == self.parent[node]:
            return node
        self.parent[node] = self.findUltimateParent(self.parent[node])
        return self.parent[node]

    def unionByRank(self, u, v):
        u_parent = self.findUltimateParent(u)
        v_parent = self.findUltimateParent(v)

        if u_parent == v_parent:
            return

        if u_parent < v_parent:
            self.parent[u_parent] = v_parent
        elif u_parent > v_parent:
            self.parent[v_parent] = u_parent

        else:
            self.parent[v_parent] = u_parent
            self.rank[u_parent] += 1

    def unionBySize(self, u, v):
        u_parent = self.findUltimateParent(u)
        v_parent = self.findUltimateParent(v)

        if u_parent == v_parent:
            return

        if u_parent < v_parent:
            self.parent[u_parent] = v_parent
            self.size[v_parent] += 1
        else:
            self.parent[v_parent] = u_parent
            self.size[u_parent] += 1


if __name__ == '__main__':
    ds = DisjointSet(7)
    func = ds.unionBySize
    func(1, 2)
    func(2, 3)
    func(4, 5)
    func(6, 7)
    func(5, 6)

    # Checking if 3 and 7 are in the same set or not
    if ds.findUltimateParent(3) == ds.findUltimateParent(7):
        print("Same")
    else:
        print("Not same")

    func(3, 7)

    # Checking if 3 and 7 are in the same set after union
    if ds.findUltimateParent(3) == ds.findUltimateParent(7):
        print("Same")
    else:
        print("Not same")
