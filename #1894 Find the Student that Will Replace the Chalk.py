from typing import List

class Solution:
    def chalkReplacer(self, chalk: List[int], k: int) -> int:
        """
        Determines which student will be using the chalk at the k-th minute.

        Args:
        chalk (List[int]): A list where each element represents the amount of chalk required by each student.
        k (int): The total number of minutes that the chalk will be used.

        Returns:
        int: The index of the student who will be using the chalk at the k-th minute.
        """
        # Total amount of chalk needed for a full round
        full_round = sum(chalk)
        
        # Remaining chalk needed after completing full rounds
        last_round = k % full_round
        
        # Iterate over the chalk list to determine who will use the chalk at minute k
        for i, s in enumerate(chalk):
            if s > last_round:
                return i
            else:
                last_round -= s
