#
# @lc app=leetcode id=901 lang=python3
#
# [901] Online Stock Span
#


# @lc code=start
class StockSpanner:
    # monotonic stack
    def __init__(self):
        self.stack = []

    def next(self, price):
        span = 1
        while self.stack and self.stack[-1][0] <= price:
            span += self.stack.pop()[1]
        self.stack.append([price, span])
        return span


class StockSpanner_naive:
    # will hit TLE because of a lot of redundant computations
    def __init__(self):
        self.prices = []

    def next(self, price: int) -> int:
        self.prices.append(price)
        span = 1
        # redundant computations will happen in the loop
        for i in range(len(self.prices) - 2, -1, -1):
            if self.prices[i] <= price:
                span += 1
            else:
                break
        return span


# Your StockSpanner object will be instantiated and called as such:
o = StockSpanner()
a = [100, 80, 60, 70, 60, 75, 85]
for p in a:
    span = o.next(p)
    print(span)

# @lc code=end
