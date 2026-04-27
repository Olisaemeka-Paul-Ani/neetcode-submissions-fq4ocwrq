# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        output = 0
        def traverse(node,maxSoFar):
            nonlocal output
            if not node:
                return 0
            if node.val >= maxSoFar:
                output = output+1
            newMax = max(maxSoFar,node.val)
            traverse(node.left,newMax)
            traverse(node.right,newMax)

        traverse(root, float('-inf'))
        return output
        