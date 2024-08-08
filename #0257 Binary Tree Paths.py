from typing import List, Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def binaryTreePaths(self, root: Optional[TreeNode]) -> List[str]:
        """
        Finds all root-to-leaf paths in a binary tree.
        
        Args:
        root (Optional[TreeNode]): The root of the binary tree.
        
        Returns:
        List[str]: A list of strings representing all root-to-leaf paths.
        """
        res = []  # List to store the final paths
        self.dfs(root, "", res)  # Start DFS from the root node
        return res
    
    def dfs(self, node: Optional[TreeNode], current_path: str, res: List[str]):
        """
        Performs a depth-first search to find all root-to-leaf paths.
        
        Args:
        node (Optional[TreeNode]): The current node in the binary tree.
        current_path (str): The path accumulated so far.
        res (List[str]): The list to store the root-to-leaf paths.
        """
        if node is None:
            return
        
        # Append the current node's value to the path
        current_path += str(node.val)
        
        # If the current node is a leaf, add the path to results
        if node.left is None and node.right is None:
            res.append(current_path)
            return
        
        # Continue the search on left and right children
        if node.left:
            self.dfs(node.left, current_path + "->", res)
        if node.right:
            self.dfs(node.right, current_path + "->", res)
