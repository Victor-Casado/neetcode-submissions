class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        letters_first_word = {}
        for letter in s:
            if(letters_first_word.get(letter) == None):
                letters_first_word[letter] = 0
            letters_first_word[letter] += 1
        
        letters_second_word = {}
        for letter in t:
            if(letters_second_word.get(letter) == None):
                letters_second_word[letter] = 0
            letters_second_word[letter] += 1
        
        keys_first = letters_first_word.keys()
        keys_second = letters_second_word.keys()

        for key in keys_first:
            if key in keys_second:
                if (letters_first_word[key] != letters_second_word[key]):
                    return False
            else:
                return False
                
        for key in keys_second:
            if key in keys_first:
                if (letters_first_word[key] != letters_second_word[key]):
                    return False
            else:
                return False
        
        return True
                
        