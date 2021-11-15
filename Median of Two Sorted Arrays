/*
Given two sorted arrays nums1 and nums2 of size m and n respectively, return the median of the two sorted arrays.

The overall run time complexity should be O(log (m+n)).


Completed: September 24, 2021
*/


class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        nums3 = [0]*(len(nums1) + len(nums2))
        nums1_index = 0
        nums2_index = 0
        for x in range(len(nums1) + len(nums2)):
            if (nums1_index == len(nums1)):
                nums3[x] = nums2[nums2_index]
                nums2_index += 1
            elif (nums2_index == len(nums2)):
                nums3[x] = nums1[nums1_index]
                nums1_index += 1
            elif nums1[nums1_index] <= nums2[nums2_index]:
                print(nums1[nums1_index])
                nums3[x] = nums1[nums1_index]
                nums1_index += 1
            else:
                print(nums2[nums2_index])
                nums3[x] = nums2[nums2_index]
                nums2_index += 1
        
        if (len(nums3) % 2) == 1:
            median = nums3[int((len(nums3)-1)/2)]
        else:
            median = (nums3[int((len(nums3)-1)/2)] + nums3[int((len(nums3)+1)/2)]) / 2
        return float(median)
