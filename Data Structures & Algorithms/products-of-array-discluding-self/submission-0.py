import math

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        zero_count = nums.count(0)
        output = []
        total_product = math.prod(nums)

        if zero_count > 1:
            for i in nums:
                output.append(0)
        
        if zero_count == 1:
            non_zero_product = 1

            for i in nums:
                if i != 0:
                    non_zero_product *= i
            for i in nums:
                if i ==0:
                    output.append(non_zero_product)
                else:
                    output.append(0)
        
        if zero_count == 0:
            for i, num in enumerate(nums):
                product = total_product // num
                output.append(product)
           
        return output