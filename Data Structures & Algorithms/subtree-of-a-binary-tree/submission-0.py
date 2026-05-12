# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        if not subRoot:
            return True
        if not root and subRoot:
            return False
        if self.isSameTree(root, subRoot):
            return True
        left = self.isSubtree(root.left,subRoot)
        right = self.isSubtree(root.right,subRoot)

        return left or right
    def isSameTree(self, node,subNode):
        if not subNode and not node:
            return True
        if not subNode and node or not node and subNode:
            return False
        if node.val != subNode.val:
            return False
        left= self.isSameTree(node.left,subNode.left)
        right= self.isSameTree(node.right,subNode.right)
        return left and right




        