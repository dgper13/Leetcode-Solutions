from typing import List, Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        """
        Given the root of a binary tree, return the level order traversal of its nodes' values. 
        (i.e., from left to right, level by level).

        Args:
        root (Optional[TreeNode]): The root node of the binary tree.

        Returns:
        List[List[int]]: A list of lists where each sublist contains the values of the nodes at that level.
        """
        results = []  # List to store the level order traversal
        if not root:
            return results

        queue = [root]  # Initialize the queue with the root node
        while queue:
            level = []  # List to store nodes at the current level
            number_of_nodes = len(queue)  # Number of nodes at the current level
            for i in range(number_of_nodes):
                node = queue.pop(0)  # Dequeue the front node
                level.append(node.val)  # Add the node's value to the current level list
                if node.left:
                    queue.append(node.left)  # Enqueue left child
                if node.right:
                    queue.append(node.right)  # Enqueue right child
            results.append(level)  # Add the current level list to the results

        return results
