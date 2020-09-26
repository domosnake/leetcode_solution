#
# @lc app=leetcode id=630 lang=python3
#
# [630] Course Schedule III
#
from typing import List
from heapq import heappush, heappop


# @lc code=start
class Solution:
    def scheduleCourse(self, courses: List[List[int]]) -> int:
        # 1. You can't take multiple courses at the same time, only 1 course at a time
        # 2. To complete a course you must be continuously taking it until it ends
        # 3. You can take the courses in any order as you see fit

        # greedy, if we can't take a course(exceed deadline)
        # we don't want to simply skip the course
        # note that our goal is to take as many courses as possible
        # instead, we want to "drop" the longest course we have taken
        # and use that gap time to take as many short courses as we can

        # sort the courses by deadline
        sorted_by_deadline = sorted(courses, key=lambda c: c[1])
        # maxheap, stores the longest course
        taken = []
        today = 0
        for course_len, deadline in sorted_by_deadline:
            # take the course, move timeline "today" forward
            today += course_len
            heappush(taken, -course_len)
            # if pass deadline, drop the longest course
            if deadline < today:
                # time travel
                today -= -taken[0]
                heappop(taken)
        return len(taken)


# @lc code=end
