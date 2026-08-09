class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagrams = {}
        for i in strs:
            sorted_item = "".join(sorted(i))
            if sorted_item not in anagrams:
                anagrams[sorted_item] = []
            anagrams[sorted_item].append(i)
        return list(anagrams.values())