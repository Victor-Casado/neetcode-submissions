class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        bestBuyPrice = [prices[0]]

        for price in prices[1:]:
            bestBuyPrice.append(min(bestBuyPrice[-1], price))

        maxProfitFound = 0
        for index, price in enumerate(prices):
            maxProfitFound = max(price - bestBuyPrice[index], maxProfitFound)

        return maxProfitFound