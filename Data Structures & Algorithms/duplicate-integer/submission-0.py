class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        counts = {}
        for num in nums:
            if counts.get(num) is None:
                counts[num] = 1
            else:
                counts[num] = counts.get(num) + 1
        
        for i in counts.values():
            if i > 1:
                return True
            
        return False