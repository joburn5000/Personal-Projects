/*
Given an integer x, return true if x is palindrome integer.

An integer is a palindrome when it reads the same backward as forward. For example, 121 is palindrome while 123 is not.


Completed: October 8, 2021
*/



class Solution:
    def isPalindrome(self, x: int) -> bool:
        a = str(x)
        for i in range(len(a)):
            if a[i] != a[-i-1]:
                return False
        return True
