class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profits = [0]
        i = 0
        j = 1
        while j < len(prices):
            if prices[i] > prices[j]:
                i = j
                j = j+1
            else:
                profits.append(prices[j]-prices[i])
                j = j+1
        return max(profits)
        