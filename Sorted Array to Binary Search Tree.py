"""
Given an integer array nums where the elements 
are sorted in ascending order, convert it to a 
height-balanced binary search tree.

A height-balanced binary tree is a binary tree 
in which the depth of the two subtrees of every 
node never differs by more than one.

Completed: 1/18/2022

"""


# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def sortedArrayToBST(self, nums):
        """
        :type nums: List[int]
        :rtype: TreeNode
        """
        
        median = (len(nums)-1)/2
        if len(nums) == 1: return TreeNode(nums[median])
        elif len(nums) == 2: return TreeNode(nums[median], right=TreeNode(nums[1]))       
        return TreeNode(nums[median], 
                            Solution.sortedArrayToBST(self, nums[0:median]), 
                            Solution.sortedArrayToBST(self, nums[median+1:len(nums)]))
