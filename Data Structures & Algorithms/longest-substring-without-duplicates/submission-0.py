class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        result = 0

        for j in range(len(s)):
            seen= set()
            for i in range(j, len(s)):
                if s[i] in seen:
                    break
                seen.add(s[i])
            result = max(result, len(seen))
        return result