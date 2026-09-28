class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagrams = {} #[array of letters] -> [string, string]

        for string in strs:
            letters = [0] * 26

            for letter in string:
                letters[ord(letter) - ord('a')] += 1

            letters = tuple(letters)
            if letters in anagrams:
                anagrams[letters].append(string)
            else:
                anagrams[letters] = [string]
        
        return list(anagrams.values())
