class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        seen = {}
        left = 0 
        longest = 0
        #get the most frequent to replace with
        for r in range(len(s)):
            if seen.get(s[r]) is None:
                seen[s[r]] = 1
            else:
                seen[s[r]] += 1
            
            most_frequent = max(seen.values())
            while (r - left + 1) - most_frequent > k:
                seen[s[left]] -=1
                left += 1
                most_frequent = max(seen.values())
            longest= max(longest, r - left + 1)
        return longest




