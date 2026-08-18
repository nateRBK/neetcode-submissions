# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []
        result = []
        val = root.val
        left = root.left
        right = root.right

        result.append(val)
        result += self.preorderTraversal(left)
        result += self.preorderTraversal(right)
        return result