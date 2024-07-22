from typing import List, Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        """
        Given the root of a binary tree, return the zigzag level order traversal of its nodes' values. 
        (i.e., from left to right, then right to left for the next level and alternate between).

        Args:
        root (Optional[TreeNode]): The root node of the binary tree.

        Returns:
        List[List[int]]: A list of lists where each sublist contains the values of the nodes at that level in zigzag order.
        """
        results = []  # List to store the zigzag level order traversal
        if not root:
            return results
        
        queue = [root]  # Initialize the queue with the root node
        normal_order = True  # Flag to determine the order of traversal for each level

        while queue:
            level = []  # List to store nodes at the current level
            number_of_nodes = len(queue)  # Number of nodes at the current level
            for i in range(number_of_nodes):
                current = queue.pop(0)  # Dequeue the front node
                level.append(current.val)  # Add the node's value to the current level list
                if current.left:
                    queue.append(current.left)  # Enqueue left child
                if current.right:
                    queue.append(current.right)  # Enqueue right child
            
            if not normal_order:
                level.reverse()  # Reverse the current level list if the order is not normal
            results.append(level)  # Add the current level list to the results
            normal_order = not normal_order  # Toggle the order for the next level

        return results
