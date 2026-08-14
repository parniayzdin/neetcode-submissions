class Solution:
    def findMin(self, nums: List[int]) -> int:

        #Reverse the array
        reversed_nums = nums[::-1] 

        #Reverse k elements where k= distanc of minimum to the end + 1
        minimum_element = min(nums)

        k = 0
        i = nums.index(minimum_element)
        while i < len(nums):
            k += 1
            i += 1
        
        reversed_nums[:k] = reversed(reversed_nums[:k]) 

        
        reversed_nums[k:] = reversed(reversed_nums[k:])

        return reversed_nums[0]
