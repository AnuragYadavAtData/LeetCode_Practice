# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        def deep(t):
            if t is None:
                return 0
            ld = deep(t.left)
            rd = deep(t.right)
            return max(ld, rd) + 1

        return deep(root)



