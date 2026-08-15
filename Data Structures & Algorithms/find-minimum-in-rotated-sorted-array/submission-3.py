class Solution:
    def findMin(self, nums: List[int]) -> int:

        lo = 0
        hi = len(nums) - 1
        minimum_element = nums[0]
        while lo <= hi:
            mid = (lo + hi) // 2

            #Left portion is sorted if
            if nums[lo] <= nums[mid]:
                minimum_element = min(minimum_element, nums[lo])
                lo = mid + 1
            #Right portion is sorted if 
            elif nums[mid] <= nums[hi]:
                minimum_element = min(minimum_element, nums[mid])
                hi = mid - 1                
        return minimum_element
        
        
        
