class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counts = {}

        for i in nums:
            if counts.get(i) is None:
                counts[i] = 1
            else:
                counts[i] = counts.get(i) + 1

        sorted_items = sorted(counts.items(), key = lambda counts: counts[1], reverse=True)
        
        result = []

        frequent = sorted_items[:k]
        for items in frequent:
            result.append(items[0])
        return result
        
        