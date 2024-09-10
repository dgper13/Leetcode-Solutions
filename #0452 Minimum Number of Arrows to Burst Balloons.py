from typing import List

class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        # Initial assumption: at least one arrow per balloon
        min_arrows = len(points)
        
        # Sort the intervals by their starting point
        points = sorted(points, key=lambda x: x[0])
        
        # Set the first interval as the previous interval
        prev = points[0]

        # Loop through the remaining intervals
        for interval in points[1:]:
            last_start, last_end = prev  # Get the previous interval's start and end
            start, end = interval        # Get the current interval's start and end

            # If there's an overlap between the current and the previous interval
            if last_end >= start:
                # Update the previous interval to the overlap range
                prev = [max(start, last_start), min(end, last_end)]
                # Reduce the arrow count since we don't need a new arrow
                min_arrows -= 1
            else:
                # No overlap, so the current interval becomes the new 'previous' interval
                prev = [start, end]

        # Return the total number of arrows needed
        return min_arrows
