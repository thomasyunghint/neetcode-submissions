"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def canAttendMeetings(self, intervals: List[Interval]) -> bool:
        isGood = True
        intervals.sort(key=lambda i: i.start)
        for i in range(len(intervals)):
            if i+1 < len(intervals):
                if intervals[i].end > intervals[i+1].start:
                    isGood = False
        return isGood