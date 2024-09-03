from typing import List


class TrieNode:
    def __init__(self):
        """
        Initialize a TrieNode with an empty dictionary for children
        and a boolean flag for marking the end of a word.
        """
        self.children = {}  # Dictionary to hold child nodes
        self.end_of_word = False  # Flag to mark the end of a word

class Trie:

    def __init__(self):
        """
        Initialize a Trie with a root TrieNode.
        """
        self.root = TrieNode()  # Root node of the Trie

    def insert(self, word: str) -> None:
        """
        Insert a word into the Trie.

        Args:
        word (str): The word to be inserted.
        """
        curr = self.root  # Start from the root node
        for c in word:
            # If the character is not in the current node's children, add it
            if c not in curr.children:
                curr.children[c] = TrieNode()
            # Move to the child node
            curr = curr.children[c]
        # Mark the end of the word at the final node
        curr.end_of_word = True


class Solution:
    def indexPairs(self, text: str, words: List[str]) -> List[List[int]]:

        trie = Trie()

        for word in words:
            trie.insert(word)


    def includes(self, word) -> List[int]:
        curr = self.root
        end = 0
        i = 0

        while i < len(word):

            if word[i] in curr.children:
                i += 1
            else:
                i = 0

            end += 1

            if not curr.end_of_word:
                next_key = next(iter(curr.children))
                curr = curr.children[next_key]
            else:
                break
        
        if i == len(word):
            return [end - i, end -1]
        return []
    

trie = Trie()
trie.insert("TaylorAlisonSwift")

words = ["katy","Taylor"]

results = []
for word in words:
    res = trie.includes(word)
    if res:
        results.append(res)

results = sorted(results, key = lambda x: (x[0], x[1]))
print(results)