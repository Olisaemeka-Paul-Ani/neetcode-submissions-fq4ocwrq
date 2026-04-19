# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        self.maxD = 0
        def traverse(node,snapshot):
            if not node:
                return
            traverse(node.left, snapshot+1)
            self.maxD = max(self.maxD,snapshot)
            traverse(node.right, snapshot+1)
        
        traverse(root,1)
        return self.maxD