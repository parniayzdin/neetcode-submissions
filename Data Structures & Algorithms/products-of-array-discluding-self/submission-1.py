import math

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        result = []

        product = math.prod(nums)
        count = 0
        for j in range(len(nums)):
            if nums[j] == 0:
                count +=1

        if count >= 2:
            for i in range(len(nums)):
                result.append(0)

        elif count == 0:
            for i in range(len(nums)):
                product1 = math.prod(x for j, x in enumerate(nums) if j != i)
                result.append(product1)
        
        else:
            for i in range(len(nums)):
                product1 = math.prod(x for j, x in enumerate(nums) if j != i)
                result.append(product1)
 
        return result
        
        

       