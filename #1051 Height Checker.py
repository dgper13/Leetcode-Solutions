from typing import List

class Solution:
    def heightChecker(self, heights: List[int]) -> int:
        """
        Count the number of students who are not standing in the correct height order.

        Given a list of student heights, this function calculates how many students
        need to move to match the correct (non-decreasing) order of heights.

        Args:
            heights (List[int]): A list of integers representing the heights of students.

        Returns:
            int: The number of students not in the correct order.
        """
        height_count = {}

        # Count occurrences of each height
        for height in heights:
            height_count[height] = height_count.get(height, 0) + 1
        
        # Generate the expected sorted order
        expected_order = []
        for height in range(min(heights), max(heights) + 1):
            expected_order.extend([height] * height_count.get(height, 0))

        # Compare actual heights with expected order
        wrong_count = 0
        for i in range(len(heights)):
            if heights[i] != expected_order[i]:
                wrong_count += 1

        return wrong_count
    