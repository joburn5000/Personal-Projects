'''
Given two binary strings a and b, return their sum as a binary string.

Completed: 12/08/2021
'''

class Solution(object):
    def addBinary(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: str
        """
        max_size = max(len(a), len(b))
        
        a = "0"*(max_size-len(a)) + a
        b = "0"*(max_size-len(b)) + b
        
        carry = 0
        output = ""
        for i in reversed(range(max_size)):
            num = int(a[i])+int(b[i])+carry
            if num > 1: carry = 1
            else: carry = 0
            output = str(num%2) + output
        if carry:
            output = str(carry) + output
        return output
