class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        minimum = prices[0]
        profit = 0

        for price in prices:
            if price < minimum:
                minimum = price
            else:
                new_profit = price - minimum

                if new_profit > profit:
                    profit = new_profit

        return profit
            
            
        

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna