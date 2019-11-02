# Input: [[1,3],[2,6],[8,10],[15,18]]
# Output: [[1,6],[8,10],[15,18]]
# Explanation: Since intervals [1,3] and [2,6] overlaps, merge them into [1,6].


def merge_intervals(intervals):

    intervals.sort(key = lambda x:x[0])
        i = 1
        while i < len(intervals):
            if intervals[i][0] <= intervals[i-1][1]:
                intervals[i-1][0] = min(intervals[i-1][0], intervals[i][0])
                intervals[i-1][1] = max(intervals[i-1][1], intervals[i][1])
                
                intervals.pop(i)
            else:
                i += 1
        return intervals

