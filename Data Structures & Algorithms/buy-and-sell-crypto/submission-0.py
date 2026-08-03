class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # define pointers
        pointer1 = 0
        pointer2 = 1
    
        # have a value that is equal to zero
        maxprofit = 0

        # iterate through the array
        for price in prices:
            # if the value is greater have it replace it
            if pointer2 != len(prices):
                if prices[pointer2] > prices[pointer1]:
                    profit = prices[pointer2] - prices[pointer1]
                    maxprofit = max(profit, maxprofit)
                else:
                    pointer1 = pointer2
            pointer2 += 1
        
        return maxprofit