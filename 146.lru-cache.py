#
# @lc app=leetcode id=146 lang=python3
#
# [146] LRU Cache
#

# @lc code=start
class LRUCache:

    # Python OrderedDict is impletmented by a double linked list
    # to preserve the insertion order
    # for this problem, let's not use build-in data structure
    # and impletment it ourselves wit a double linked list
    # list head being LRU, tail being MRU
    def __init__(self, capacity: int):
        self.capacity = capacity
        # key to double linked node
        self.cache = {}
        # double linked list
        self.head = Node(0, 0)
        self.tail = Node(0, 0)
        self._connect(self.head, self.tail)

    def get(self, key: int) -> int:
        if key not in self.cache:
            return -1
        self._remove(self.cache[key])
        self._addAtTail(self.cache[key])
        return self.cache[key].value

    def put(self, key: int, value: int) -> None:
        # set
        if key in self.cache:
            self._remove(self.cache[key])
            self._addAtTail(self.cache[key])
            self.cache[key].value = value
        # insert
        else:
            if len(self.cache) >= self.capacity:
                # remove LRU item from cache and list
                del self.cache[self.head.next.key]
                self._remove(self.head.next)
            # add new item to cache and list
            self.cache[key] = Node(key, value)
            self._addAtTail(self.cache[key])

    # below are double linked list operations
    def _remove(self, node):
        self._connect(node.prev, node.next)

    def _addAtTail(self, node):
        self._connect(self.tail.prev, node)
        self._connect(node, self.tail)

    def _connect(self, prevNode, nextNode):
        prevNode.next = nextNode
        nextNode.prev = prevNode


class Node:
    def __init__(self, key: int, value: int):
        self.key = key
        self.value = value
        self.prev = None
        self.next = None

# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)
# @lc code=end
