class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        
        result = set()
        event_horizon = set()

        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):
                total = nums[i] + nums[j]

                if -total in event_horizon:
                    create_triplet = [-total, nums[i], nums[j]]
                    sorted_triplet = sorted(create_triplet)
                    tuple_tri = tuple(sorted_triplet) #sets cannot store lists so we turn it into tuple (-1, 0, 2)
                    result.add(tuple_tri)
            event_horizon.add(nums[i]) #this is saved for future, because i might become -total for a pair, so we save it
        return list(result)
