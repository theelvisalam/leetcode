'''
You are given an integer array prices where prices[i] is the price of NeetCoin on the ith day.

You may choose a single day to buy one NeetCoin and choose a different day in the future to sell it.

Return the maximum profit you can achieve. You may choose to not make any transactions, in which case the profit would be 0.

Example 1:

Input: prices = [10,1,5,6,7,1]

Output: 6

Explanation: Buy prices[1] and sell prices[4], profit = 7 - 1 = 6.

Example 2:

Input: prices = [10,8,7,5,2]

Output: 0

Explanation: No profitable transactions can be made, thus the max profit is 0.
'''
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if prices is None:
            return 0
        
        currProfit = 0

        for i in range(0, len(prices)):
            for j in range(i + 1, len(prices)):
                print(f"j: {prices[j]} | i: {prices[i]}")
                if prices[j] - prices[i] <= 0:
                    continue
                # elif currProfit > 0 and prices[j] - prices[i] <= 0:
                #     break
                else:
                    currProfit += prices[j] - prices[i]                
                    # print(prices[j] - prices[i])
                # print(currProfit)
        return currProfit

prices = [10,1,5,6,7,1]
sol = Solution()
print(sol.maxProfit(prices))
