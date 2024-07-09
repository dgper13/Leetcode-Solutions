from typing import List

class Solution:
    def averageWaitingTime(self, clients: List[List[int]]) -> float:
        """
        Calculate the average waiting time for a list of clients.

        Each client is represented by a list of two integers, where the first integer 
        is the arrival time and the second integer is the preparation time.

        Args:
        clients (List[List[int]]): A list of clients, where each client is a list 
                                   containing the arrival time and preparation time.

        Returns:
        float: The average waiting time of all clients.
        """
        
        total_waiting_time = 0
        current_time = 0

        for arrival_time, prep_time in clients:
            # Determine the actual start time for the current client
            actual_start_time = max(arrival_time, current_time)

            # Calculate finish time for the current client
            finish_time = actual_start_time + prep_time

            # Calculate waiting time for the current client
            waiting_time = finish_time - arrival_time

            # Update total waiting time
            total_waiting_time += waiting_time

            # Update current time to the finish time of the current client
            current_time = finish_time
            
        # Calculate and return the average waiting time
        return total_waiting_time / len(clients)
