from typing import List

class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        # Step 1: Sort the intervals by their starting time.
        intervals = sorted(intervals, key=lambda x: x[0])

        # Step 2: Initialize the result list with the first interval.
        res = [intervals[0]]

        # Step 3: Iterate over the remaining intervals starting from the second one.
        for start, end in intervals[1:]:
            # Get the end of the last interval in the result list.
            last_end = res[-1][1]

            # Step 4: If the current interval overlaps with the last interval in the result list:
            if start <= last_end:
                # Merge the intervals by updating the end of the last interval in the result list.
                res[-1][1] = max(last_end, end)
            else:
                # Otherwise, add the current interval to the result list as a separate interval.
                res.append([start, end])
        
        # Step 5: Return the merged list of intervals.
        return res
