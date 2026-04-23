# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []
        output, queue = [], deque([root])
        currRight = "None"
        while queue:
            i, lenQ = 0, len(queue)
            while i < lenQ:
                node = queue.popleft()
                currRight = node.val
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
                i=i+1
            output.append(currRight)
        return output