from typing import List

class Solution:
    def lemonadeChange(self, bills: List[int]) -> bool:
        """
        This function determines whether we can provide the correct change to every customer in line.
        
        Args:
        bills (List[int]): List of bills given by customers, which can be 5, 10, or 20.

        Returns:
        bool: True if it's possible to provide the correct change for every customer, False otherwise.
        """

        five = 0  # Number of $5 bills
        ten = 0   # Number of $10 bills

        for bill in bills:
            if bill == 5:
                five += 1  # Collect the $5 bill

            elif bill == 10:
                ten += 1  # Collect the $10 bill
                change = 5  # The change needed is $5
                if five > 0:  # If we have a $5 bill for change
                    five -= 1  # Give $5 as change
                else:  # If we don't have a $5 bill to give as change
                    return False

            else:  # If the bill is $20
                change = 15  # The change needed is $15
                # Prefer to give one $10 bill and one $5 bill as change
                if five > 0 and ten > 0:
                    five -= 1  # Give one $5 bill as change
                    ten -= 1  # Give one $10 bill as change
                elif five >= 3:  # If we don't have a $10 bill, give three $5 bills as change
                    five -= 3  # Give three $5 bills as change
                else:  # If we cannot provide the correct change
                    return False

        return True  # If we can give the correct change to all customers, return True
