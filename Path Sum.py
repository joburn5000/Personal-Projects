'''
Given the root of a binary tree and an integer targetSum, 
return true if the tree has a root-to-leaf path such that 
adding up all the values along the path equals targetSum.

Completed: 12/08/2021
'''

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def hasPathSum(self, root, targetSum):
        """
        :type root: TreeNode
        :type targetSum: int
        :rtype: bool
        """
        if not root: return False
        
        #recursive function
        def pathSum(self, node, s, flag):
            if not node.left and not node.right: # leaf
                if s == targetSum: return True
            else:
                if node.left:
                    if pathSum(self, node.left, s+node.left.val, flag): return True
                if node.right:
                    if pathSum(self, node.right, s+node.right.val, flag): return True
                return False
                
        return pathSum(self, root, root.val, False)
        
                
                
            
        
        
