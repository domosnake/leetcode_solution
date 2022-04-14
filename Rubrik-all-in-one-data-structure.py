# Design a data structure with following functions
# class DataStructure:
#   public:
#     # Insert val to the set, return True if element is added succesfully
#     bool insert(int val)
#     # Remove val from the set, return True if element is removed successfully
#     bool remove(int, val)
#     # Get a random element from the set
#     int getRandom()
#     # Check if the val exists in the set
#     bool exists(int val)
#     # return LRU, insert(), getRandom(), exists() should update the usage
#     int getLRU()

from random import choice


class DataStructure:

    def __init__(self) -> None:
        # val to node map
        self._data = {}
        # doubly linked list to track usage
        self._dll = DLL()
        # list for random
        self._list = []
        # val to index map
        self._index = {}

    def insert(self, val: int) -> bool:
        if val in self._data:
            return False
        node = Node(val)
        # add to data
        self._data[val] = node
        # update usage
        self._dll.insertAtTail(node)
        # add to list
        self._list.append(val)
        self._index[len(self._list) - 1] = val
        return True

    def remove(self, val: int) -> bool:
        if val not in self._data:
            return False
        node = self._data[val]
        # remove val from map and dll
        self._dll.remove(node)
        del self._data[val]
        # remove val from list and index
        i = self._index[val]
        # update index
        self._index[self._list[-1]] = i
        # swap for quick popping
        self._list[i], self._list[-1] = self._list[-1], self._list[i]
        self._list.pop()
        del self._index[val]

    def getRandom(self, val: int) -> int:
        pick = choice(self._list)
        self._updateUsage(pick)
        return pick

    def exists(self, val: int) -> bool:
        found = val in self._data
        if found:
            self._updateUsage(val)
        return found

    def getLRU(self) -> int:
        # head of DLL
        lru_node = self._dll.first()
        return lru_node.val

    def _updateUsage(self, val: int):
        # remve and add to tail
        node = self.data[val]
        self.list.remove(node)
        self.list.insertAtTail(node)


class Node:
    def __init__(self, val) -> None:
        self.val = val
        self.next = None
        self.prev = None


# doubly linked list
class DLL:
    def __init__(self) -> None:
        self._head = Node(-1)
        self._tail = Node(-1)
        self._connect(self._heed, self._tail)

    def remove(self, node):
        self._connect(node.prev, node.next)
        node.prev = None
        node.next = None

    def insertAtTail(self, node):
        self._connect(self.tail.prev, node)
        self._connect(node, self.tail)

    # return first node in the list
    def first(self):
        return self._head.next

    def _connect(self, prevNode, nextNode):
        prevNode.next = nextNode
        nextNode.prev = prevNode
