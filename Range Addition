/*
You are given an m x n matrix M initialized with all 0's and an array of operations ops,
where ops[i] = [ai, bi] means M[x][y] should be incremented by one for all 0 <= x < ai and 0 <= y < bi.

Count and return the number of maximum integers in the matrix after performing all the operations.


Completed: September 1, 2021
*/

class Solution(object):
    def maxCount(self, m, n, ops):
        """
        :type m: int
        :type n: int
        :type ops: List[List[int]]
        :rtype: int
        """
        min_x = n
        min_y = m
        for i in range(len(ops)):
            if ops[i][0] < min_y:
                min_y = ops[i][0]
            if ops[i][1] < min_x:
                min_x = ops[i][1]

        return min_y * min_x
            
        
