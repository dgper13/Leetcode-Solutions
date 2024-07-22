from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def getMinimumDifference(self, root: Optional[TreeNode]) -> int:
        """
        Given a binary search tree (BST), find the minimum absolute difference between
        the values of any two nodes.

        Args:
        root (Optional[TreeNode]): The root of the binary search tree.

        Returns:
        int: The minimum absolute difference between the values of any two nodes.
        """
        prev = [None]  # List to hold the value of the previously visited node
        res = [float("inf")]  # List to hold the minimum difference found

        def dfs(node: Optional[TreeNode]) -> None:
            """
            Perform in-order traversal to find the minimum difference.

            Args:
            node (Optional[TreeNode]): The current node in the binary search tree.
            """
            if not node:
                return

            # Traverse the left subtree
            dfs(node.left)

            # Process the current node
            if prev[0] is not None:
                res[0] = min(res[0], node.val - prev[0])
            prev[0] = node.val

            # Traverse the right subtree
            dfs(node.right)

        # Start the DFS traversal from the root
        dfs(root)
        return res[0]
