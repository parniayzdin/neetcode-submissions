class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        maxProfit = 0; 
        
        for i in range(len(prices)): #i is for buying
            for j in range(i + 1, len(prices)): #j is for selling
                profit = prices[j] - prices[i]
                maxProfit = max(maxProfit, profit)
        return maxProfit



        