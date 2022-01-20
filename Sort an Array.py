"""
Given an array of integers nums, sort the array in ascending order.

Example 1:

Input: nums = [5,2,3,1]
Output: [1,2,3,5]
Example 2:

Input: nums = [5,1,1,2,0,0]
Output: [0,0,1,1,2,5]


Completed: 1/19/2022
"""

class Solution(object):
    def sortArray(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        
        if len(nums) == 1: return nums
        
        median = (len(nums)+1)/2
        arr1 = Solution.sortArray(self,nums[:median])
        arr2 = Solution.sortArray(self,nums[median:])
        
        combined_arr = []
        while (len(arr1) > 0) | (len(arr2) > 0):
            if (len(arr2) == 0):
                combined_arr.append(arr1[0])
                arr1 = arr1[1:]
            elif (len(arr1) == 0):
                combined_arr.append(arr2[0])
                arr2 = arr2[1:]
            else:
                if arr1[0] < arr2[0]:
                    combined_arr.append(arr1[0])
                    arr1 = arr1[1:]
                else:
                    combined_arr.append(arr2[0])
                    arr2 = arr2[1:]
        
        return combined_arr
        
        
        """
        Other recursive method:
        
        if len(nums) == 1: return nums
        if len(nums) == 2: return nums if nums[0] < nums[1] else nums[::-1]
        
        array = Solution.sortArray(self, nums[1:])
        
        if nums[0] < array[0]: 
            return [nums[0]]+ array
        
        for i in range(len(array))[::-1]:
            if nums[0] > array[i]: 
                array.insert(i+1,nums[0])
                return array
        """
