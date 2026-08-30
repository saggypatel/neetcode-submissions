# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        # if not root:
        #     return 0
        depth = 0
        stack = [root]
        while stack:
            child = []
            while stack:
                top = stack.pop()
                if top.left:
                    child.append(top.left)
                if top.right:
                    child.append(top.right)
            stack = child
            depth += 1
        return depth