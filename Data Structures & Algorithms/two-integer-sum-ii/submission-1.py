class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        result = []
        numbers.insert(0,None)

        i = 1
        j = len(numbers)-1
        while i <= j:
            if numbers[i] + numbers[j] == target:
                result.append(i)
                result.append(j)
                return result
            elif numbers[i] + numbers[j] > target:
                j -= 1
            else:
                i+=1
        return 