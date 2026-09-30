class Solution:
    def countSubstrings(self, s: str) -> int:
        count = 0

        for index, character in enumerate(s):
            #odd
            leftIndex = index
            rightIndex = index
            while(leftIndex >= 0 and rightIndex < len(s) and s[leftIndex] == s[rightIndex]):
                count += 1
                leftIndex -= 1
                rightIndex += 1

            #even
            leftIndex = index
            rightIndex = index + 1
            while(leftIndex >= 0 and rightIndex < len(s) and s[leftIndex] == s[rightIndex]):
                count += 1
                leftIndex -= 1
                rightIndex += 1
        
        return count