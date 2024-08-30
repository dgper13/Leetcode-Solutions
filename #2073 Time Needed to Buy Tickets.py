from typing import List

class Solution:
    def timeRequiredToBuy(self, tickets: List[int], k: int) -> int:
        """
        Calculates the time required for the k-th person to buy their ticket.

        Args:
        tickets (List[int]): A list where `tickets[i]` is the number of tickets the i-th person wants to buy.
        k (int): The index of the k-th person in the list.

        Returns:
        int: The time required for the k-th person to buy their ticket.
        """
        time = 0  # Initialize total time required
        buyers = len(tickets)  # Total number of people in the queue
        k_tickets = tickets[k]  # Number of tickets the k-th person wants to buy

        # Iterate over each person in the queue
        for i in range(buyers):
            if i < k:
                # For people before the k-th person, they will buy up to k_tickets
                time += min(tickets[i], k_tickets)
            elif i == k:
                # The k-th person will buy all their tickets
                time += k_tickets
            else:
                # For people after the k-th person, they will buy up to k_tickets - 1
                time += min(tickets[i], k_tickets - 1)
        
        return time
