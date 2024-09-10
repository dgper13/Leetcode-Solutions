from typing import List

class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        
        # Find the position to insert the new interval using binary search
        def find_insert_position(intervals: List[List[int]], newInterval: List[int]) -> int:
            low, high = 0, len(intervals) - 1
            while low <= high:
                mid = (low + high) // 2
                if intervals[mid][0] < newInterval[0]:
                    low = mid + 1
                else:
                    high = mid - 1
            return low

        # If there are no intervals, just return the newInterval
        if not intervals:
            return [newInterval]

        # Find the insert position
        pos = find_insert_position(intervals, newInterval)
        # Insert newInterval at the correct position
        intervals.insert(pos, newInterval)

        # Result list to store merged intervals
        res = [intervals[0]]
        
        # Iterate through the intervals to merge them
        for interval in intervals[1:]:
            last_start, last_end = res[-1]
            start, end = interval

            # If intervals overlap, merge them
            if last_end >= start:
                res[-1] = [min(start, last_start), max(end, last_end)]
            else:
                res.append([start, end])
        
        return res
