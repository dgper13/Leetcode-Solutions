from typing import List

class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        # Step 1: Sort the intervals based on their starting times.
        intervals = sorted(intervals, key=lambda x: x[0])
        
        # Step 2: Initialize the count of intervals to remove and the end of the last added interval.
        res = 0
        prev_end = intervals[0][1]

        # Step 3: Iterate over the intervals starting from the second one.
        for start, end in intervals[1:]:
            # Step 4: If the current interval does not overlap with the previous one
            if start >= prev_end:
                # Update the end to the end of the current interval.
                prev_end = end
            else:
                # If overlapping, increment the removal count.
                res += 1
                # Update the end to the minimum of the current interval's end and the previous end.
                # This ensures that we consider the interval with the earliest end to minimize overlap.
                prev_end = min(end, prev_end)
        
        # Step 5: Return the total number of intervals to remove.
        return res
