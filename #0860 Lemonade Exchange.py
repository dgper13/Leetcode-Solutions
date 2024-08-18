from typing import List

class Solution:
    def lemonadeChange(self, bills: List[int]) -> bool:
        """
        This function determines if it's possible to provide the correct change to each customer in line
        given the bills provided in the `bills` list.

        Args:
        bills (List[int]): A list of integers representing the bills given by customers.

        Returns:
        bool: True if all customers can be given correct change, False otherwise.
        """

        five = 0  # Counter for $5 bills
        ten = 0   # Counter for $10 bills

        for bill in bills:
            if bill == 5:
                five += 1  # Increment the $5 bill counter when a $5 bill is received

            elif bill == 10:
                ten += 1  # Increment the $10 bill counter when a $10 bill is received

            change = bill - 5  # Calculate the change required

            if change == 5:  # If the required change is $5
                if five > 0:  # Check if there is a $5 bill available
                    five -= 1  # Give out a $5 bill as change
                else:
                    return False  # Return False if unable to provide the correct change

            if change == 15:  # If the required change is $15
                if five > 0 and ten > 0:  # Prefer to give out one $10 bill and one $5 bill as change
                    five -= 1
                    ten -= 1
                elif five >= 3:  # Alternatively, give out three $5 bills as change
                    five -= 3
                else:
                    return False  # Return False if unable to provide the correct change

        return True  # If the loop completes, all customers were given correct change
