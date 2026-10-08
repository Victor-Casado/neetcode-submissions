# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        #search tree until we find same starting val
        #compare equality
        compareTrees = self.findValues(root, subRoot.val, []) #subroot.val is safe, we are given at least 1 node in subRoot tree
        for tree in compareTrees:
            if (self.areEqualTrees(tree, subRoot)):
                return True
        
        return False

    def areEqualTrees(self, p, q):
        if ((p is None) != (q is None)):
            return False
        if (p is None):
            return True
        
        if (p.val != q.val):
            return False

        if ((p.left is None) != (q.left is None)):
            return False
        if ((p.right is None) != (q.right is None)):
            return False
        if ((p.left is None) and (p.right is None)):
            return True
        
        return self.areEqualTrees(p.left, q.left) and self.areEqualTrees(p.right, q.right)

    def findValues(self, tree, valueToFind, valuesFound):
        if (tree is None):
            return valuesFound
        
        if (tree.val == valueToFind):
            valuesFound.append(tree)
        
        self.findValues(tree.left, valueToFind, valuesFound)
        self.findValues(tree.right, valueToFind, valuesFound)
        return valuesFound