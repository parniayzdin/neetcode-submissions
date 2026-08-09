import string
class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = s.translate(str.maketrans("", "", string.punctuation))
        s= "".join(s.split())
        s= s.lower()

        left = 0            #since you assigned numbers to them,
                            #th string will automatically be represented as indices
        right = len(s) - 1


        while left < right:
            if s[left] != s[right]:
                return False
            left += 1
            right -= 1
        return True 
            

        