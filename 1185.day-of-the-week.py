#
# @lc app=leetcode id=1185 lang=python3
#
# [1185] Day of the Week
#


# @lc code=start
class Solution:
    def dayOfTheWeek(self, day: int, month: int, year: int) -> str:
        # should have given the starting condition
        # 1971-01-01 is Friday
        WEEKDAY = [
            'Friday', 'Saturday', 'Sunday', 'Monday',
            'Tuesday', 'Wednesday', 'Thursday'
        ]
        MONTH_DAY = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

        # year
        year_days = 0
        for y in range(1971, year):
            year_days += 366 if self.isLeadYear(y) else 365

        # month
        month_days = 0
        for m in range(1, month):
            month_days += MONTH_DAY[m - 1]
        if month > 2:
            month_days += 1 if self.isLeadYear(year) else 0

        # today
        today = year_days + month_days + (day - 1)
        return WEEKDAY[today % 7]

    def isLeadYear(self, year: int) -> bool:
        if year <= 0:
            return False
        # normal leap year
        if year % 4 == 0:
            # 2000 is a leap year, 1900 is not
            if year % 100 == 0:
                return year % 400 == 0
            else:
                return True
        return False


# s = Solution()
# a = s.dayOfTheWeek(29, 2, 2016)
# print(a)

# @lc code=end
