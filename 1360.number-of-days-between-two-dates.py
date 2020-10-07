#
# @lc app=leetcode id=1360 lang=python3
#
# [1360] Number of Days Between Two Dates
#


# @lc code=start
class Solution:
    def daysBetweenDates(self, date1: str, date2: str) -> int:
        # date is YYYY-MM-DD
        return abs(self.daysSince1971(date1) - self.daysSince1971(date2))

    def daysSince1971(self, date: str) -> int:
        MONTH_DAY = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

        int_date = [int(d) for d in date.split('-')]
        # year
        year_days = 0
        for y in range(1971, int_date[0]):
            year_days += 366 if self.isLeapYear(y) else 365

        # month
        month_days = 0
        for m in range(1, int_date[1]):
            month_days += MONTH_DAY[m - 1]
        if int_date[1] > 2:
            month_days += 1 if self.isLeapYear(int_date[0]) else 0

        # today
        return year_days + month_days + (int_date[2] - 1)

    def isLeapYear(self, year: int) -> bool:
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


# @lc code=end
