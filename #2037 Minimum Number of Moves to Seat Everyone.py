from typing import List

class Solution:
    def minMovesToSeat(self, seats: List[int], students: List[int]) -> int:
        # Sort the lists to minimize movement
        seats.sort()
        students.sort()
        
        total_moves = 0
        
        # Calculate the total moves needed by summing up the absolute differences
        for i in range(len(students)):
            total_moves += abs(students[i] - seats[i])
        
        return total_moves
