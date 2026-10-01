class Solution:
    def numDecodings(self, s: str) -> int:
        #notes:
        '''
        27+ cannot be a number
        0x means previous was 20, 30.
        We will never see 40, 50, etc

        I'm thinking split along 0s, 27+s into subsections
        Each subsection will have no invalid pairings
        
        Amount of ways per subsection is amount with n-1 + amount w n-2
        If you have 4 there are 5 ways
        If you have 5 there are 8 ways
        If you have 8 there are 8 ways + new ways enabled by 6th (6th is part of pair, and thus 4 free to play with so 5)
        '''

        count = 1
        sections = [] #coords of sections [first, last]
        startingSectionIndex = 0
        for index, character in enumerate(s):
            if(character == '0'):

                if(index == startingSectionIndex):
                    #invalid
                    return 0

                if(int(s[index - 1]) > 2):
                    return 0

                sections.append([startingSectionIndex, index - 2])
                startingSectionIndex = index + 1

            if (index + 1 < len(s) and int(s[index:index + 2]) > 26):
                sections.append([startingSectionIndex, index])
                startingSectionIndex = index + 1
            

        sections.append([startingSectionIndex, len(s) - 1])
        
        for section in sections:
            length = section[1] - section[0] + 1
            count *= self.getCombos(length)
        
        return count


    def getCombos(self, n: int) -> int:
        if n <= 1:
            return 1

        prev2 = 1
        prev1 = 1

        for iter in range(2, n + 1):
            curr = prev1 + prev2
            prev2 = prev1
            prev1 = curr

        return prev1