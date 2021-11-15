/*
Write a function to find the longest common prefix string amongst an array of strings.
If there is no common prefix, return an empty string

Completed: October 8, 2021
*/

class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        i = 0
        done = False
        if strs == "":
            return ""
        while i<len(strs[0]):
            for word in strs:
                if (i>=len(word)):
                    done = True
                    break
                if word[i] != strs[0][i]:
                    done = True
                    break
            if done:
                break
            i+=1
        return strs[0][0:i]
