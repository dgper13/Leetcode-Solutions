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

    def search(self, word: str) -> bool:
        """
        Search for a word in the Trie.

        Args:
        word (str): The word to search for.

        Returns:
        bool: True if the word exists in the Trie, False otherwise.
        """
        curr = self.root  # Start from the root node
        for c in word:
            # If the character is not in the current node's children, the word does not exist
            if c not in curr.children:
                return False
            # Move to the child node
            curr = curr.children[c]
        # Return True if the end of the word is marked
        return curr.end_of_word

    def startsWith(self, prefix: str) -> bool:
        """
        Check if there is any word in the Trie that starts with the given prefix.

        Args:
        prefix (str): The prefix to check for.

        Returns:
        bool: True if there is a word starting with the prefix, False otherwise.
        """
        curr = self.root  # Start from the root node
        for c in prefix:
            # If the character is not in the current node's children, the prefix does not exist
            if c not in curr.children:
                return False
            # Move to the child node
            curr = curr.children[c]
        # Return True if the prefix was found
        return True
