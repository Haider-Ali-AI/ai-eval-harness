class Solution:
    def maxProfit(self, prices: list[int]) -> int:
        profit = 0
        minimum = prices[0]
        Max_P = 0

        for price in prices:
            if price < minimum:
                minimum = price

            profit = price - minimum
            Max_P = max(Max_P, profit)

        return Max_P