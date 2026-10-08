# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:

        if ((p is None) != (q is None)): #None checks
            return False
        if (p is None):
            return True
        
        if (p.val != q.val): #Value checks
            return False
        
        if ( (p.left is None) != (q.left is None) ): #children checks
            return False
        if ( (p.right is None) != (q.right is None) ):
            return False
        
        if(p.left is None and p.right is None): #if no children
            return True

        return self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)
        