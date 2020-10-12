#
# @lc app=leetcode id=1507 lang=python3
#
# [1507] Reformat Date
#


# @lc code=start
class Solution:
    def reformatDate(self, date: str) -> str:
        if not date:
            return ''
        MONTH = {
            'Jan': '01',
            'Feb': '02',
            'Mar': '03',
            'Apr': '04',
            'May': '05',
            'Jun': '06',
            'Jul': '07',
            'Aug': '08',
            'Sep': '09',
            'Oct': '10',
            'Nov': '11',
            'Dec': '12'
        }
        parts = date.split(' ')
        day = parts[0][:2]
        day = day if day.isdigit() else '0' + day[0]
        return parts[2] + '-' + MONTH[parts[1]] + '-' + day


# @lc code=end
