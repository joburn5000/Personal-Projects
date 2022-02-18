"""
Roman numerals are represented by seven different symbols: I, V, X, L, C, D and M.

Symbol       Value
I             1
V             5
X             10
L             50
C             100
D             500
M             1000

For example, 2 is written as II in Roman numeral, just two one's added together. 
12 is written as XII, which is simply X + II. The number 27 is written as XXVII, 
which is XX + V + II.

Roman numerals are usually written largest to smallest from left to right. 
However, the numeral for four is not IIII. Instead, the number four is written 
as IV. Because the one is before the five we subtract it making four. The same 
principle applies to the number nine, which is written as IX. There are six 
instances where subtraction is used:

I can be placed before V (5) and X (10) to make 4 and 9. 
X can be placed before L (50) and C (100) to make 40 and 90. 
C can be placed before D (500) and M (1000) to make 400 and 900.
Given an integer, convert it to a roman numeral.

 

Example 1:

Input: num = 3
Output: "III"
Explanation: 3 is represented as 3 ones.
Example 2:

Input: num = 58
Output: "LVIII"
Explanation: L = 50, V = 5, III = 3.
Example 3:

Input: num = 1994
Output: "MCMXCIV"
Explanation: M = 1000, CM = 900, XC = 90 and IV = 4.
 
Difficulty: medium
Completed: 2/18/2022

"""


class Solution(object):
    def intToRoman(self, num):
        """
        :type num: int
        :rtype: str
        """
        # 1000 or more      M per 1000
        # 900               CM 
        # 500 < x < 900     DC
        # 400               CD
        # 100 < x < 400     C per 100
        #
        # 90                XC 
        # 50 < x < 90       LX
        # 40                XL
        # 10 < x < 40       X per 10
        
        # 9                 IX 
        # 5 < x < 9         VI
        # 4                 IV
        # 1 < x < 4         I per 1
        
        def digitToRoman(self, digit, power):
            """
            :type digit: int
            :type power: int
            :rtype: str
            """
            output, ten, five, one= "", "", "", ""
            if power == 1:
                ten = "C"
                five = "L"
                one = "X"
            elif power == 0:
                ten = "X"
                five = "V"
                one = "I"
            else:
                ten = "M"
                five = "D"
                one = "C"
            
            if digit == 9:
                output = one + ten
            elif digit >= 5:
                output = five + one*(digit-5)
            elif digit == 4:
                output = one + five
            else:
                output = one*digit
        
            return output
        
        n = num
        s = digitToRoman(self, n%10, 0)
        n = n/10
        if n == 0: return s
        s = digitToRoman(self, n%10, 1) + s
        n = n/10
        if n == 0: return s
        s = digitToRoman(self, n%10, 2) + s
        n = n/10
        if n == 0: return s
        s = "M"*n + s
        return s
        
                    
                    
