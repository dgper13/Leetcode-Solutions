class Solution:
    def addBinary(self, a: str, b: str) -> str:
        res = []      # List to store the result digits
        carry = 0     # Initialize carry for addition

        a = a[::-1]   # Reverse the strings to start addition from the least significant bit
        b = b[::-1]

        # Loop through the maximum length of the two strings
        for i in range(max(len(a), len(b))):
            # Get the current digits from each string or use 0 if index is out of bounds
            digit_a = int(a[i]) if i < len(a) else 0
            digit_b = int(b[i]) if i < len(b) else 0

            # Calculate total of digits and carry
            total = digit_a + digit_b + carry
            res.append(str(total % 2))  # Append the result digit (binary)
            carry = total // 2          # Update carry

        # If there is any carry left, append it
        if carry:
            res.append("1")
        
        res.reverse()  # Reverse the result list to the original order

        return "".join(res)  # Join list into a string and return
