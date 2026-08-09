import re
class Solution:

    def encode(self, strs: List[str]) -> str:
        encode = ""
        for i in strs:
            encode += str(len(i)) + "#" + i 
        return encode
        
    def decode(self, s: str) -> List[str]:

        i = 0
        result = []
        while i < len(s):
            j = s.find("#", i)
            length = int(s[i:j])
            word_start = j + 1
            word_end = word_start + length
            result.append(s[word_start:word_end])

            i= word_end
        
        return result

        
