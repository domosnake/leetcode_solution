#
# @lc app=leetcode id=146 lang=python3
#
# [146] LRU Cache
# Design a data structure that follows the constraints of a Least Recently Used (LRU) cache.
#
# Implement the LRUCache class:
#
# LRUCache(int capacity) Initialize the LRU cache with positive size capacity.
# int get(int key) Return the value of the key if the key exists, otherwise return -1.
# void put(int key, int value) Update the value of the key if the key exists.
# Otherwise, add the key-value pair to the cache.
# If the number of keys exceeds the capacity from this operation, evict the least recently used key.
# The functions get and put must each run in O(1) average time complexity.

# @lc code=start


class LRUCache:

    # Python OrderedDict is impletmented by a double linked list
    # to preserve the insertion order
    # for this problem, let's not use build-in data structure
    # and impletment it ourselves wit a double linked list
    # list head being LRU, tail being MRU
    def __init__(self, capacity: int):
        if capacity <= 0:
            raise ValueError('Please pass in a positive number for capacity')
        self.capacity = capacity
        # key to double linked node
        self.cache = {}
        # double linked list
        self.list = DoublyLinkedList()

    def get(self, key: int) -> int:
        if key not in self.cache:
            return -1
        self._renew(key)
        return self.cache[key].value

    def put(self, key: int, value: int) -> None:
        # set
        if key in self.cache:
            self._renew(key)
            self.cache[key].value = value
        # insert
        else:
            if len(self.cache) >= self.capacity:
                # remove LRU item from cache and list
                self._evict()
            # add new item to cache and list
            self.cache[key] = Node(key, value)
            self._new(key)

    def _evict(self):
        oldest = self.list.head.next
        del self.cache[oldest.key]
        self.list.remove(oldest)

    def _renew(self, key: int):
        self.list.remove(self.cache[key])
        self._new(key)

    def _new(self, key: int):
        self.list.addAtTail(self.cache[key])


class DoublyLinkedList:
    def __init__(self) -> None:
        # dummy head and tail for safeguarding
        self.head = Node(0, 0)
        self.tail = Node(0, 0)
        self._connect(self.head, self.tail)

    # below are double linked list operations
    def remove(self, node):
        self._connect(node.prev, node.next)

    def addAtTail(self, node):
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
