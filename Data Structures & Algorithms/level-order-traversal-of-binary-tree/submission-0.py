class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []
        queue = deque([root])
        output = []

        while queue:
            level = []
            i = 0
            lenLevel = len(queue)
            while i < lenLevel:
                node = queue.popleft()
                level.append(node.val)
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
                i=i+1
            output.append(level)
        return output
        