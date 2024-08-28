from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        balanced = [True]  # A list is used to keep track of the balanced state

        def height(node):
            if not node:
                return 0

            left = height(node.left)
            if not balanced[0]:
                return 0

            right = height(node.right)

            if abs(left - right) > 1:
                balanced[0] = False
                return 0
            
            return 1 + max(left, right)

        height(root)
        return balanced[0]
