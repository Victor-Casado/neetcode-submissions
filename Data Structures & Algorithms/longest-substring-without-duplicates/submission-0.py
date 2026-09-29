import string

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        letter_dict = dict.fromkeys(string.printable, -1)
        maxLengthFound = 0
        lastRepeat = -1

        for index, char in enumerate(s):
            if letter_dict[char] != -1:
                lastRepeat = max(lastRepeat, letter_dict[char])
            
            maxLengthFound = max(maxLengthFound, index - max(letter_dict[char], lastRepeat))
            letter_dict[char] = index

        return maxLengthFound