# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        self.pArr = []
        self.qArr = []

        def traverse(node, arr):
            if not node:
                arr.append("null")
                return
            arr.append(node.val)
            traverse(node.left,arr)
            traverse(node.right,arr)
        traverse(p,self.pArr)
        traverse(q,self.qArr)

        return self.pArr == self.qArr
        
        