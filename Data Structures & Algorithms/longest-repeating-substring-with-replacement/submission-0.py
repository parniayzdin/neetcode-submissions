class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        longest = 0
        seen = {}
        left = 0
        most_frequent = 0
        count = k #capture the amoutn of changes until it reaches zero

        for r in range(len(s)):

            # first we need to know the frequency of each so that we replace the characters with the most frequent characters
            if seen.get(s[r]) is None:
                seen[s[r]] = 1
            else:
                seen[s[r]] = seen.get(s[r]) + 1
            most_frequent = max(seen.values())

            while (r - left + 1) - most_frequent > k:
                seen[s[left]] -= 1 #since the characer is leaving the window reduce its count
                left  += 1
                most_frequent = max(seen.values())
                
            longest = max(longest, r - left + 1)
        
        return longest   
