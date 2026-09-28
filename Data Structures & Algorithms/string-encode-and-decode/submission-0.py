class Solution:

    def encode(self, strs: List[str]) -> str:
        #use 'a' as separator
        #if an 'a' exists, use "aa"
        result = ""
        
        for string in strs:
            result += str(len(string))
            result += "a"
            result += string

        return result

    def decode(self, s: str) -> List[str]:
        decoded_strings = []
        current_position = 0

        while current_position < len(s):
            separator_position = current_position

            # Find the 'a' that separates the length from the string
            while s[separator_position] != 'a':
                separator_position += 1

            # Read the number before the separator
            string_length = int(s[current_position:separator_position])

            # The actual string starts right after the separator
            string_start = separator_position + 1
            string_end = string_start + string_length

            decoded_string = s[string_start:string_end]
            decoded_strings.append(decoded_string)

            # Move to the start of the next encoded string
            current_position = string_end

        return decoded_strings