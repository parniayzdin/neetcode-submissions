class Solution:
    def isAnagram(self, s: str, t: str) -> bool:

        if len(s) != len(t):
            return False
            
        counts1 = {}
        counts2 = {}

        for char in s:
            if counts1.get(char) is None:
                counts1[char] = 1
            else:
                counts1[char] = counts1.get(char) + 1
        
        for char in t:
            if counts2.get(char) is None:
                counts2[char] = 1
            else:
                counts2[char] = counts2.get(char) + 1
        
        if counts2 == counts1:
            return True
        else:
            return False
        