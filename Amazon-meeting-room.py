# Given an array of meeting time intervals consisting of start and end times [[s1,e1],[s2,e2],...]
# find the minimum number of conference rooms required.
from typing import List
from heapq import heappush, heappop


class Solution:
    # meeting room I: can a person attend all meetings?
    # Input: [[0,30],[5,10],[15,20]]
    # Output: false
    #
    # Input: [[7,10],[2,4]]
    # Output: true
    def canAttend(self, intervals: List[List[int]]) -> bool:
        # check if any adjacent intervals has overlap
        # sort the intervals by start time
        sortedIntervals = sorted(intervals, key=lambda i: i[0])
        for i in range(1, len(sortedIntervals)):
            prevEnd = sortedIntervals[i-1][1]
            nextStart = sortedIntervals[i][0]
            if nextStart < prevEnd:
                return False
        return True

    # meeting room II: minimum number of conference rooms required
    # Input: [[0, 30],[5, 10],[15, 20]]
    # Output: 2

    # Input: [[7,10],[2,4]]
    # Output: 1
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        if not intervals:
            return 0
        sortedIntervals = sorted(intervals, key=lambda i: i[0])
        # minheap
        meetingEndTimes = []
        for interval in sortedIntervals:
            nextMeetingEndTime = interval[1]
            nextMeetingStartTime = interval[0]
            # if next meeting start time later than earliest meeting end time
            # it means they can be held in the same room
            if meetingEndTimes:
                earliestMeetingEndTime = meetingEndTimes[0]
                if nextMeetingStartTime >= earliestMeetingEndTime:
                    # room is already used in last meeting and continue to use the same room for this meeting
                    # thus, extend the end time
                    heappop(meetingEndTimes)
            heappush(meetingEndTimes, nextMeetingEndTime)
        return len(meetingEndTimes)


s = Solution()
times = [[0, 14], [3, 7], [9, 12], [5, 10], [15, 20]]
a = s.canAttend(times)
print(a)
a = s.minMeetingRooms(times)
print(a)
