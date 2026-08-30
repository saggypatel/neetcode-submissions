class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit = 0
        for i,m in enumerate(prices):
            for j,n in enumerate(prices):
                if (j <= i):
                    continue
                
                if prices[j] > prices[i]:
                    profit = max(profit, prices[j] - prices[i])
        
        return profit
        