# 1.
# An engineer can only handle a fixed number of tasks a day. Design a data strcutre to simulate the to-do-list.
# Tasks are handled on a FIFO basis. Tasks are unique.
#
# The data structure needs to expose below APIs:
# void add(string task) # O(1) performance, raise an error if limit is reached
# void handle() # O(1) performance, a task is handled and removed from the to-do-list
# string print() # print the data structure, so we know which tasks are in the list, and in which order
# void promote() # get a promotion hence number of tasks can be handled is increased
# void prioritize(string task) # prioritize the task despite FIFO,
# task is handled and removed from the to-do-list. Can you achieve O(1) time?
# write test code to validate the APIs
# discuss thread-safety of the APIs


class Node:
    def __init__(self, val):
        self.val = val
        self.prev = None
        self.next = None


class DoublyLinkedList:
    def __init__(self):
        # dummy head and tail for safeguarding
        self._head = Node('H')
        self._tail = Node('T')
        self._connect(self._head, self._tail)
        self._size = 0

    @property
    def size(self) -> int:
        return self._size

    @property
    def head(self) -> Node:
        if self._size > 0:
            return self._head.next
        else:
            return None

    def append(self, node):
        self._connect(self._tail.prev, node)
        self._connect(node, self._tail)
        self._size += 1

    def remove(self, node):
        self._connect(node.prev, node.next)
        self._size -= 1

    # helper to connect 2 nodes
    def _connect(self, prevNode, nextNode):
        prevNode.next = nextNode
        nextNode.prev = prevNode


class TaskManager:
    def __init__(self, capacity):
        if capacity <= 0:
            raise ValueError('Capacity must be a postive integer')
        self._capacity = capacity
        # task in to tail, task out from head
        self._list = DoublyLinkedList()
        # quick task lookup
        self._table = {}

    def add(self, task: str):
        if self._list.size >= self._capacity:
            print(f'Cannot add task {task}. Tasks reached capacity')
        else:
            node = Node(task)
            self._list.append(node)
            # tasks are unique
            self._table[task] = node

    def handle(self):
        if self._list.size > 0:
            oldest_task = self._list.head.val
            self._removeTask(oldest_task)

    # rename to printTasks as print is a reserved key word in python
    def printTasks(self):
        if self._list.size <= 0:
            print('No task')
        else:
            cur = self._list.head
            i = 0
            tasks = []
            while i < self._list.size:
                tasks.append(cur.val)
                i += 1
                cur = cur.next
            print('Tasks are handled in below order:')
            print(' -> '.join(tasks))

    def promote(self):
        self._capacity *= 2

    def prioritize(self, task):
        self._removeTask(task)

    # helper to remove a task from table and list
    def _removeTask(self, task):
        if not task or task not in self._table:
            print(f'Task {task} not found')
        else:
            # remove task from table and list
            node = self._table[task]
            del self._table[task]
            self._list.remove(node)


# test
tm = TaskManager(3)
tm.add('Check email')
tm.add('Fix a bug')
tm.add('Planing')
tm.printTasks()  # Check email -> Fix a bug -> Planing
tm.add(
    'Team building')  # Cannot add task Team building. Tasks reached capacity
tm.promote()  # 3 -> 6
tm.add('Lunch')
tm.add('Meeting')
tm.add('Team building')
tm.printTasks(
)  # Check email -> Fix a bug -> Planing -> Lunch -> Meeting -> Team building
tm.handle()  # remove Check email
tm.handle()  # remove Fix a bug
tm.printTasks()  # Planing -> Lunch -> Meeting -> Team building
tm.add('Handle p0 issue')
tm.add('1-on-1 meeting')
tm.printTasks(
)  # Planing -> Lunch -> Meeting -> Team building -> Handle p0 issue -> 1-on-1 meeting
tm.prioritize('Buy coffee')  # Task Buy coffee not found
tm.prioritize('Handle p0 issue')  # remove Handle p0 issue
tm.printTasks(
)  # Planing -> Lunch -> Meeting -> Team building -> 1-on-1 meeting
