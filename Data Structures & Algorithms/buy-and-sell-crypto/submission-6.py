class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_profit=0
        L=0
        R=1
        while R<len(prices): # 
            profit=prices[R]-prices[L]
            if profit<=0:
                L=R
                R+=1
            else : 
                R+=1
                max_profit=max(max_profit,profit)
        return max_profit
        