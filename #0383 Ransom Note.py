class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        if len(ransomNote) > len(magazine):
            return False
        
        letter_count = {}
        
        # Count occurrences of each character in magazine
        for l in magazine:
            letter_count[l] = letter_count.get(l, 0) + 1
        
        # Check if ransomNote can be constructed
        for l in ransomNote:
            if letter_count.get(l, 0) > 0:
                letter_count[l] -= 1
            else:
                return False
        
        return True
    