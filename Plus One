/*
You are given a large integer represented as an integer array digits, where each digits[i] is the ith digit of the integer. 
The digits are ordered from most significant to least significant in left-to-right order. The large integer does not contain any leading 0's.

Increment the large integer by one and return the resulting array of digits.

Completed: 11/27/2021
*/



class Solution(object):
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        carry = True
        for i in reversed(range(len(digits))):
            if !carry: break
            if digits[i] != 9:
                carry = False
            digits[i] = (digits[i]+1) % 10
        
        if carry:
            digits = [1] + digits
            
        return digits
        
