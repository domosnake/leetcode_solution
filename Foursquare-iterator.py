from collections import deque


class Iterator:
    def __init__(self, arr):
        self.arr = arr
        self.i = 0

    def hasNext(self):
        return self.i < len(self.arr)

    def next(self):
        cur = self.arr[self.i]
        self.i += 1
        return cur


# Multi-iterator - using queue
class MultiIterator(Iterator):
    def __init__(self, iters):
        if not iters or len(iters) == 0:
            raise Exception('Iterator list is empty, please verify the input')
        self.iters = iters
        self.q = deque()
        for i in self.iters:
            if i.hasNext():
                self.q.append(i)

    def next(self):
        if not self.hasNext():
            raise Exception('No more items to return')
        cur = self.q[0]
        return cur.next()

    def hasNext(self):
        while self.q:
            cur = self.q[0]
            if cur.hasNext():
                return True
            else:
                self.q.popleft()

        return False


# 交错式
class InterleavingIterator(Iterator):
    def __init__(self, iters):
        if not iters or len(iters) == 0:
            raise Exception('Iterator list is empty, please verify the input')
        self.iters = iters
        self.q = deque()
        for i in self.iters:
            if i.hasNext():
                self.q.append(i)

    def next(self):
        if not self.hasNext():
            raise Exception('No more items to return')
        cur = self.q.popleft()
        self.q.append(cur)
        return cur.next()

    def hasNext(self):
        while self.q:
            cur = self.q[0]
            if cur.hasNext():
                return True
            else:
                self.q.popleft()

        return False


iters = [Iterator([1, 2, 3]), Iterator([4]), Iterator([]), Iterator([7, 8, 9])]
a = MultiIterator(iters)
while a.hasNext():
    print(a.next())

print('---------')
iters = [
    Iterator([]),
    Iterator([1, 2, 3]),
    Iterator([4, 5]),
    Iterator([7, 8, 9])
]
b = InterleavingIterator(iters)
while b.hasNext():
    print(b.next())
