class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        N = len(prices)

        i = j = 0
        profit = 0
        while i < N and j < N-1:
            j += 1
            if prices[i] > prices[j]:
                i = j
                continue
                   
            profit = max(profit, prices[j] - prices[i])

        return profit
