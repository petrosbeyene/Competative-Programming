# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def tree2str(self, root: Optional[TreeNode]) -> str:
        if not root:
            return ""
        
        left = self.tree2str(root.left)
        right = self.tree2str(root.right)

        if left == "" and right == "":
            return str(root.val)
        elif left == "":
            return str(root.val) + "()" + "(" + right + ")"
        elif right == "":
            return str(root.val) + "(" + left + ")"
        else:
            return str(root.val) + "(" + left + ")" + "(" + right + ")"
        
        
        
