# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isMirror(self, p, q):
        if p == None and q == None:
            return True
        if (p and not q) or (q and not p) or (p.val != q.val):
            return False

        return self.isMirror(p.left, q.right) and self.isMirror(p.right, q.left)
    
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        return self.isMirror(root.left, root.right)
