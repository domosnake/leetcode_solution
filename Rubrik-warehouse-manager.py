# 2.
# Design a data structure that can track the items and the quantity stored in a warehouse.
# The data structure also provides audit capability. An audit is a frozen view of the status of the warehouse at a given day.
# Audit can be defined as you see fit.
#
# Please note that the key requirement for this data structure is space efficiency (Hint: data deduplication).
# Time complaxity is also important, but space can not be sacrificed for more speed.
# The data structure needs to expose below APIs:
# void put(string item)
# void remove(string item)
# int get(string item)
# int getFromAudit(string item, Audit day)
# Audit audit()
# void deleteAudit(Audit day)

# # Example:
# put('A')
# put('A')
# put('A')
# put('B')
# put('B')
# audit() -> day1 # A = 3, B = 2
# get('A') -> 3
# put('C')
# remove('A')
# audit() -> day2 # A = 2, B = 2, C = 1
# remove('C')
# getFromAudit('B', day2) -> 2
# getFromAudit('C', day2) -> 1
# getFromAudit('C', day1) -> Error, item C not found in the warehouse on day1
# get('C') -> Error, item C not found in the warehouse currently
# deleteAudit(day1)
# getFromAudit('A', day1) -> Error, audit day1 not found


class Stock:
    def __init__(self, des='Stock'):
        self._des = des

    @property
    def description(self) -> str:
        return self._des


# daily audit, but it's essentially a snapshot with timestamp
class Audit(Stock):
    def __init__(self, day: int):
        super().__init__('Audit')
        self._day = day

    @property
    def day(self) -> str:
        return f'day_{self._day}'


# the purpose of this class is to show that we dedup data by pointing to same object
class ItemCount:
    def __init__(self, item: str, count: int):
        self._item = item
        self.count = count

    @property
    def item(self):
        return self._item


# 1. use a map of map track item count and audits
# 2. do not copy data, use pointer to point to the same object
# 3. we can generalize to snapshots with timestamp. hence audits are a subset
# 4. time: deleteAudit() and audit() are O(n), the rest are O(1)
# 5. space: number of items + number of audits * k (delta from last audit)
class WarehouseManager:
    def __init__(self):
        # {item -> {Audit -> ItemCount}}
        self._data = {}
        # audits
        self._audits = set()
        # base key
        self._stock = Stock()
        # base day
        self._day = 1

    def put(self, item: str):
        if item not in self._data:
            self._data[item] = {}
        # upsert item count
        if self._stock not in self._data[item]:
            self._data[item][self._stock] = ItemCount(item, 1)
        else:
            cur_count = self._data[item][self._stock].count
            self._data[item][self._stock] = ItemCount(item, cur_count + 1)

    def get(self, item: str) -> int:
        if item not in self._data or self._stock not in self._data[item]:
            raise KeyError(f'Item {item} not found in the warehouse currently')
        return self._data[item][self._stock].count

    def getFromAudit(self, item: str, audit: Audit) -> int:
        # no audit
        if audit not in self._audits:
            raise KeyError(f'Audit {audit.day} not found')
        if item not in self._data or audit not in self._data[item]:
            raise KeyError(f'Item {item} not found in the Audit {audit.day}')
        return self._data[item][audit].count

    def remove(self, item: str):
        if item not in self._data or self._stock not in self._data[item]:
            raise KeyError(f'Item {item} not found in the warehouse currently')
        # check current item stock
        cur_count = self._data[item][self._stock].count
        # delete item stock if count is 0
        if cur_count - 1 <= 0:
            del self._data[item][self._stock]
            # also remember to delete item
            if len(self._data[item]) == 0:
                del self._data[item]
        else:
            self._data[item][self._stock] = ItemCount(item, cur_count - 1)

    def deleteAudit(self, audit: Audit):
        if audit in self._audits:
            self._audits.remove(audit)
        item_to_delete = []
        for item, audit_map in self._data.items():
            # delete audit
            if audit in audit_map:
                del audit_map[audit]
            # remember to delete item, note: ConcurrentModificationException
            if len(audit_map) == 0:
                item_to_delete.append(item)
        for item in item_to_delete:
            del self._data[item]

    def audit(self) -> Audit:
        audit = Audit(self._day)
        self._audits.add(audit)
        # inc day
        self._day += 1
        # for each item currently in the warehouse, create audit with dedupped data
        for audit_map in self._data.values():
            if self._stock in audit_map:
                cur_stock = audit_map[self._stock]
                audit_map[audit] = cur_stock
        return audit

    # helper print function for testing
    def printAudit(self, audit):
        items = []
        for audit_map in self._data.values():
            if audit in audit_map:
                # item count
                ic = audit_map[audit]
                # <item>(<object id>) = <count>
                items.append(f'{ic.item}({id(ic)}) = {ic.count}')
        print(f'{audit.day}: {", ".join(items)}')


# test
wm = WarehouseManager()
wm.put('A')
wm.put('A')
wm.put('A')
wm.put('B')
wm.put('B')
day1 = wm.audit()
wm.printAudit(day1)  # day_1: A(28046552) = 3, B(28046648) = 2
assert wm.get('A') == 3
wm.put('C')
wm.remove('A')
day2 = wm.audit()
wm.printAudit(day2)  # day_2: A(28046744) = 2, B(28046648) = 2, C(28046696) = 1
day3 = wm.audit()
wm.printAudit(day3)  # day_3: A(28046744) = 2, B(28046648) = 2, C(28046696) = 1
wm.remove('C')
day4 = wm.audit()
wm.printAudit(day4)  # day_4: A(28046744) = 2, B(28046648) = 2
assert wm.getFromAudit('B', day2) == 2
assert wm.getFromAudit('C', day2) == 1
try:
    wm.getFromAudit('C', day1)
except Exception as e:
    print(e)  # Item C not found in the Audit day_1
try:
    wm.get('C')
except Exception as e:
    print(e)  # Item C not found in the warehouse currently
wm.deleteAudit(day1)
try:
    wm.getFromAudit('A', day1)
except Exception as e:
    print(e)  # Audit day_1 not found
assert wm.get('A') == 2
assert wm.get('B') == 2
