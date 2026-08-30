# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if not root:
            return None

        queue = deque([root])
        # queue.append(root)

        while queue:
            top = queue.popleft()

            top.left, top.right = top.right, top.left

            if top.left:
                queue.append(top.left)
            if top.right:
                queue.append(top.right)
        return root


        # root.left, root.right = root.right, root.left

        # self.invertTree(root.left)
        # self.invertTree(root.right)

        # return root