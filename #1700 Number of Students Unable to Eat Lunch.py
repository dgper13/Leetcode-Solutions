from typing import List
from collections import Counter

class Solution:
    def countStudents(self, students: List[int], sandwiches: List[int]) -> int:
        # Count the number of students preferring each type of sandwich (0 or 1)
        cnt = Counter(students)

        # Iterate through each sandwich in the given order
        for sandwich in sandwiches:
            # If there are students preferring the current sandwich
            if cnt[sandwich] > 0:
                cnt[sandwich] -= 1  # Serve the sandwich and reduce the count
            else:
                # If no student wants the current sandwich, return the number of remaining students
                return cnt[0] + cnt[1]
        
        # If all sandwiches are served, return 0 as no students are left
        return cnt[0] + cnt[1]
