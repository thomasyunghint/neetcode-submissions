class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_profit=0
        lowest=1000
        for i in range(0, len(prices)):
            curr_profit = prices[i]- lowest
            max_profit=max(max_profit, curr_profit)
            lowest = min(lowest, prices[i])
        return max_profit
