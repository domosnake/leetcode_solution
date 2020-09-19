# Given a list of weighted edges between nodes, find the minimum cost spanning tree.
from typing import List
from heapq import heappop, heappush


class Edge:
    def __init__(self, v1: int, v2: int, weight: int):
        self.v1 = v1
        self.v2 = v2
        self.weight = weight


class QuickUnionFind:
    def __init__(self, vertexNum: int):
        self.count = vertexNum
        self.weight = [0] * vertexNum
        self.node_id = [0] * vertexNum
        for i in range(vertexNum):
            self.node_id[i] = i
            self.weight[i] = 1

    # 查找x所属的连通分量
    def find(self, x: int) -> int:
        while x != self.node_id[x]:
            # path compression, set parent id to grand parent id
            self.node_id[x] = self.node_id[self.node_id[x]]
            # 若找不到，则一直往根root回溯
            x = self.node_id[x]
        return x

    # 连接p,q(将q的分量改为p所在的分量)
    def union(self, p: int, q: int):
        pID = self.find(p)
        qID = self.find(q)
        # already connected, return
        if pID == qID:
            return

        # weighted quick union
        # check weight of 2 trees, always attach small tree to big tree for balance(quick union)
        # if p tree is smaller
        if self.weight[pID] < self.weight[qID]:
            # connect p to q
            self.node_id[pID] = qID
            # thus, increase q tree weight
            self.weight[qID] += self.weight[pID]
        # if q tree is smaller
        else:
            # connect q to p
            self.node_id[qID] = pID
            # thus, increase p tree weight
            self.weight[pID] += self.weight[qID]
        # one less group
        self.count -= 1

    # 判断p,q是否连接，即是否属于同一个分量
    def isConnected(self, p: int, q: int) -> bool:
        return self.find(p) == self.find(q)


class Solution:
    # add edge
    def MST_Kruskal(self, edges: List[Edge]) -> int:
        # basically, given a weighted, connected and undirected graph
        # we are to find the weight of minimum spanning tree(s)
        # note that such graph can have more than one minimum spanning tree
        #
        # Kruskal’s algorithm - greedy
        # always pick the edge with min weight
        # 1. sort edges by weight
        # 2. pick edge with min weight, if no cycle deteced, add the edge to MST
        # 3. repeat (2)
        # 4. stop when all edges are checked
        mst_weight = 0
        # this is the minimum spanning tree
        mst = []

        sortedEdges = sorted(edges, key=lambda e: e.weight)
        # vertex to id map
        vertexIdMap = {}
        i = 0
        for edge in edges:
            if edge.v1 not in vertexIdMap:
                vertexIdMap[edge.v1] = i
                i += 1
            if edge.v2 not in vertexIdMap:
                vertexIdMap[edge.v2] = i
                i += 1

        uf = QuickUnionFind(len(vertexIdMap))

        # check all edges
        for edge in sortedEdges:
            p = vertexIdMap[edge.v1]
            q = vertexIdMap[edge.v2]
            if not uf.isConnected(p, q):
                uf.union(p, q)
                mst.append(edge)
                mst_weight += edge.weight

        return mst_weight

    # add vertices
    def MST_Lazy_Prim(self, edges: List[Edge]) -> int:
        # Lazy Prim’s algorithm - greedy
        # 1. start from source
        # 2. add all edges of the current vertex priority queue
        # 3. pick edge with min weight
        # 4. add connecting vertex to mst, and mark vertex visited
        # 5. stop when all vertices are checked
        mst_weight = 0
        mst = []
        # build adjacency list
        vertices = {}
        for edge in edges:
            if edge.v1 not in vertices:
                vertices[edge.v1] = [(edge.weight, edge.v2)]
            else:
                vertices[edge.v1].append((edge.weight, edge.v2))
            if edge.v2 not in vertices:
                vertices[edge.v2] = [(edge.weight, edge.v1)]
            else:
                vertices[edge.v2].append((edge.weight, edge.v1))

        pq = []
        start = edges[0].v1
        visited = {start}
        mst.append(start)
        # pick a source vertex and add it's edges to pq
        for v in vertices[start]:
            heappush(pq, (v[0], v[1]))

        while pq:
            weight, connectTo = heappop(pq)
            if connectTo in visited:
                continue
            mst_weight += weight
            mst.append(connectTo)
            visited.add(connectTo)
            for v in vertices[connectTo]:
                if v[1] in visited:
                    continue
                heappush(pq, (v[0], v[1]))
        return mst_weight


s = Solution()
data = [[1, 2, 3],
        [1, 3, 5],
        [1, 5, 7],
        [2, 4, 4],
        [2, 5, 2],
        [3, 4, 8],
        [3, 5, 6]]
edges = [Edge(d[0], d[1], d[2]) for d in data]
a = s.MST_Kruskal(edges)
print(a)
a = s.MST_Lazy_Prim(edges)
print(a)
