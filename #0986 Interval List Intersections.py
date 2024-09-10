from typing import List

class Solution:
    def intervalIntersection(self, firstList: List[List[int]], secondList: List[List[int]]) -> List[List[int]]:
        # If either of the lists is empty, return an empty result list
        if not firstList or not secondList:
            return []
        
        # Initialize result list and pointers for both lists
        res = []
        p1 = p2 = 0

        # Loop while both pointers are within their respective lists
        while p1 < len(firstList) and p2 < len(secondList):
            # Get the current intervals from both lists
            start1, end1 = firstList[p1]
            start2, end2 = secondList[p2]

            # If first interval starts after the second one ends, increment p2
            if start1 > end2:
                p2 += 1
            # If second interval starts after the first one ends, increment p1
            elif start2 > end1:
                p1 += 1
            else:
                # There is an overlap; calculate the intersection
                res.append([max(start1, start2), min(end1, end2)])
                # Move the pointer for the interval that finishes first
                if end1 > end2:
                    p2 += 1
                else:
                    p1 += 1
            
        # Return the result list containing the intersections
        return res
