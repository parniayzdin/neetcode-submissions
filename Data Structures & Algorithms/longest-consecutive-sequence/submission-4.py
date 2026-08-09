class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        longest = 1
        count = 1
        if len(nums) == 0:
            return 0

        sorted_nums = sorted(nums)

        for i in range(len(sorted_nums) - 1):
            if sorted_nums[i+1] - sorted_nums[i] == 1:
                count += 1
            elif sorted_nums[i+1] == sorted_nums[i]:
                continue
            else:
                count = 1
            longest = max(longest, count)
        return longest