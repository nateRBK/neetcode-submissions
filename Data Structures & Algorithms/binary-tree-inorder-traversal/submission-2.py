# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []
        result = []
        val = root.val
        left = root.left
        right = root.right
        if not left and not right:
            result.append(val)
        elif left and not right:
            result += self.inorderTraversal(left)
            result.append(val)
        elif right and not left:
            result.append(val)
            result += self.inorderTraversal(right)
        elif right and left:
            result += self.inorderTraversal(left)
            result.append(val)
            result += self.inorderTraversal(right)
        return result