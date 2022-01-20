"""
Given an integer array nums, return all the triplets 
[nums[i], nums[j], nums[k]] such that i != j, i != k, 
and j != k, and nums[i] + nums[j] + nums[k] == 0.

Notice that the solution set must not contain duplicate 
triplets.

"""

class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        
        # brute force:
        
        if len(nums) <3: return []
        result = []
        for i in range(len(nums)-2):
            for j in range(1,len(nums)-1):
                for k in range(2, len(nums)):
                    if ((nums[i]+nums[j]+nums[k]) == 0):
                        array = [nums[i],nums[j],nums[k]]
                        array.sort()
                        if not array in result:
                            result.append(array)
        return result
