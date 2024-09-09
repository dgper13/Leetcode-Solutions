class Solution:
    def maxNumberOfBalloons(self, text: str) -> int:
        # Dictionary to store the required frequency of each letter in "balloon"
        balloon = {}
        for letter in "balloon":
            balloon[letter] = balloon.get(letter, 0) + 1
        
        # Dictionary to store the frequency of each letter in the input `text`
        text_letters = {}
        for letter in text:
            text_letters[letter] = text_letters.get(letter, 0) + 1

        res = float("inf")  # Start with infinity, as we will minimize this value
        # Compare the frequency of each letter in `balloon` and `text_letters`
        for letter in balloon:
            # Calculate how many times this letter can contribute to the word "balloon"
            res = min(res, text_letters.get(letter, 0) // balloon[letter])
            # If any letter's count is insufficient to form "balloon", return 0 early
            if res == 0:
                return res
        
        # Return the maximum number of times "balloon" can be formed
        return res
