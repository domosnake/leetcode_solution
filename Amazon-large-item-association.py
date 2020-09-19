from typing import List

# Return the largest association of items
# Input:    ['item1', 'item2']
#           ['item3', 'item4']
#           ['item4', 'item5']
# Output:   ['item3', 'item4', 'item5']
# Explaination: There 2 associated groups: ['item1', 'item2'] and ['item3', 'item4', 'item5']
#               Group ['item3', 'item4', 'item5'] is the largest, return the list lexicographically


class UnionFind:
    def __init__(self, N: int):
        self.count = N
        # weight of nodes
        self.weight = [0] * N
        # node id
        self.node_id = [0] * N
        for i in range(N):
            self.node_id[i] = i
            # each node has same weight
            self.weight[i] = 1

    # 返回连通分量数
    def getCount(self) -> int:
        return self.count

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
    def connected(self, p: int, q: int) -> bool:
        return self.find(p) == self.find(q)

    # func to find groups with max size, may find multiple groups
    def findMaxGroups(self) -> [int]:
        max_weight = 0
        max_index = []
        for i, w in enumerate(self.weight):
            # find a new max weight
            if w > max_weight:
                max_weight = w
                max_index = [i]
            # same max weight, add the index
            elif w == max_weight:
                max_index.append(i)
            # smaller weight, continue
            else:
                continue
        return max_index


class Solution:
    def largestItemAssociation(self,
                               itemAssociation: List[List[str]]) -> List[str]:
        if len(itemAssociation) == 0:
            return []
        # weightedUnionFind
        # but need to turn str to int for uid
        dic = {}
        item_i = 0
        for i in range(len(itemAssociation)):
            one = itemAssociation[i][0]
            two = itemAssociation[i][1]
            # each item has an uid
            if one not in dic:
                dic[one] = item_i
                item_i += 1
            if two not in dic:
                dic[two] = item_i
                item_i += 1
        # build unionfind
        uf = UnionFind(len(dic))
        # connect items
        for i in range(len(itemAssociation)):
            one_id = dic[itemAssociation[i][0]]
            two_id = dic[itemAssociation[i][1]]
            uf.union(one_id, two_id)

        # find max item association
        max_groups = uf.findMaxGroups()
        # map index back to item string
        res = []
        for i in max_groups:
            g = []
            for k, v in dic.items():
                if uf.find(v) == i:
                    g.append(k)
            res.append(sorted(g))
        res = sorted(res)
        return res[0]


s = Solution()
a = s.largestItemAssociation([['item1', 'item2'], ['item3', 'item4'],
                              ['item4', 'item5']])
print(a)

a = s.largestItemAssociation([['item2', 'item1'], ['item2', 'item3'],
                              ['item4', 'item5']])
print(a)

a = s.largestItemAssociation([['item20', 'item11'], ['item7', 'item8'],
                              ['item30', 'item110']])
print(a)

a = s.largestItemAssociation([['item89', 'item2'], ['item3', 'item2'],
                              ['item4', 'item3'], ['item7', 'item8'],
                              ['item8', 'item9'], ['item9', 'item10']])
print(a)

a = s.largestItemAssociation([['item1', 'item1'], ['item3', 'item3'],
                              ['item4', 'item5']])
print(a)
