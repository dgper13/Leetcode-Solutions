from typing import List

class Interval:
    def __init__(self, start: int, end: int):
        """
        Initialize an Interval object.

        Args:
        start (int): The start time of the interval.
        end (int): The end time of the interval.
        """
        self.start = start
        self.end = end

class Solution:
    def can_attend_meetings(self, intervals: List[Interval]) -> bool:
        """
        Determine if a person can attend all meetings without overlap.

        Given a list of intervals representing meeting times, this method checks if 
        a person can attend all the meetings without any overlap. The person can 
        attend all meetings if no two meetings overlap.

        Args:
        intervals (List[Interval]): A list of Interval objects where each interval 
                                     represents a meeting time with a start and end.

        Returns:
        bool: True if the person can attend all meetings without overlap, False otherwise.
        """
        # Sort intervals based on the start time
        intervals = sorted(intervals, key=lambda x: x.start)
        
        # Check for any overlapping intervals
        for i in range(1, len(intervals)):
            # If the start time of the current interval is less than the end time of the previous interval
            if intervals[i].start < intervals[i-1].end:
                return False
        
        return True
