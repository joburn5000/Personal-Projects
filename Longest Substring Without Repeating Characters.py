/*
Given a string s, find the length of the longest substring without repeating characters.

Completed: September 24
*/

# V1 very basic design: (slow)

# loop through every letter as starting letter
# make a string that holds longest substring
# check for duplicate letter
# when a duplicate letter is found, check the string length
# if string length is greater than length, replace length
# restart substring from next place
    # for more efficient, use an array that holds longest lengths for an index (later)

'''     if (s == ""):
            length = 0
        else:
            length = 1 
            
        # length of longest substring
        for x in range(len(s)-1):
            substring = s[x]
            print("." + substring + ".")
            i = x+1
            while (s[i] in substring) == False:
                substring += s[i]
                i+=1
                if i == len(s):
                    break
            if len(substring) > length:
                length = len(substring)
        return length'''
        

# V2: more advanced design: (fast)

# make a number that holds highest length. highest_length = 0
# make a substring that holds first letter. call it substring = s[0]
# a) loop through, starting with second letter and ending when you reach the end of the string
# if the letter is not in substring, add it to the substring and go to next letter
# if the letter is in the substring, then:
    # find the index of the first instance of the duplicate. call it d_index
    # compare substring length to highest length so far
    # if substring length is bigger than highest_length, replace
    # resize substring substring = substring[(d_index+1)::len(substring)]
    # repeat from a

        
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if (s == ""): return 0
        substring = s[0]
        highest_length = 1
        for x in range(1,len(s)):
            if (s[x] in substring):
                highest_length = max(highest_length, len(substring))
                substring = substring[(substring.index(s[x])+1):len(substring)] # resize
            substring += s[x]
        return max(highest_length, len(substring))



    
