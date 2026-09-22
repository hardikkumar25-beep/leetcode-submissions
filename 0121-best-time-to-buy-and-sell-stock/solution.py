class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        profit=0
        left=0
        for right in range(len(prices)):
            if prices[right]<prices[left]:
                left=right
            else:
                current=prices[right]-prices[left]
                profit=max(profit,current)
        return profit
        
