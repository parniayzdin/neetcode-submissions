class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return 0

        sorted_items = sorted(nums)

        current_count = 1
        max_count = 1

        i = 0

        while i < len(sorted_items) - 1:
            if sorted_items[i + 1] == sorted_items[i]:
                pass  # skip duplicate
            elif sorted_items[i + 1] - sorted_items[i] == 1:
                current_count += 1
            else:
                current_count = 1

            max_count = max(max_count, current_count)
            i += 1

        return max_count