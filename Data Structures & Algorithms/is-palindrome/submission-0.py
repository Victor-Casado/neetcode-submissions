class Solution:
    def isPalindrome(self, s: str) -> bool:

        sCleaned = re.sub(r'[^a-zA-Z0-9]', '', s.lower())
        for index in range(len(sCleaned) // 2):
            if(sCleaned[index] != sCleaned[len(sCleaned) - 1 -index]):
                return False
        return True