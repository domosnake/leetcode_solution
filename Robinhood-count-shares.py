from typing import List
from heapq import heappush, heappop


class Solution:
    def countOrderShares(self, orders: List[List[str]]) -> int:
        if not orders:
            return 0
        if len(orders) < 2:
            return 0
        # order[i] = [price, share, type]
        # ("150", "10", "buy")
        # ("165", "7", "sell")
        # ("168", "3", "buy")
        # ("155", "5", "sell")
        # ("166", "8", "buy")
        # return -> 11
        #
        # buy >= sell
        # if buy order, best order is a sell with min price
        # if sell order, best order is a buy with max price
        # thus, buys is max heap and sells is min heap
        buys = []
        sells = []
        total = 0
        for o in orders:
            # str -> int
            o = [int(o[0]), int(o[1]), o[2]]
            # buy order
            if o[2] == 'buy':
                while sells:
                    # check price
                    if o[0] >= sells[-1][0]:
                        s = heappop(sells)[1]
                        trade = min(o[1], s[1])
                        s[1] -= trade
                        o[1] -= trade
                        total += trade
                        # if it has some remaining shares
                        # push the sell order back to sell tracker
                        if s[1] > 0:
                            heappush(sells, (s[0], s))
                        if o[1] == 0:
                            break
                    else:
                        break
                # push buy order to buy tracker
                if o[1] > 0:
                    heappush(buys, (-o[0], o))
            # sell order
            else:
                while buys:
                    # check price
                    if buys[-1][0] >= o[0]:
                        b = heappop(buys)[1]
                        trade = min(o[1], b[1])
                        b[1] -= trade
                        o[1] -= trade
                        total += trade
                        # if it has some remaining shares
                        # push the buy order back to buy tracker
                        if b[1] > 0:
                            heappush(buys, (-b[0], b))
                        if o[1] == 0:
                            break
                    else:
                        break
                # push sell order to sell tracker
                if o[1] > 0:
                    heappush(sells, (o[0], o))
        return total


s = Solution()
orders = [["150", "10", "buy"],
          ["165", "7", "sell"],
          ["168", "3", "buy"],
          ["155", "5", "sell"],
          ["166", "8", "buy"]]
a = s.countShares(orders)
print(a)
