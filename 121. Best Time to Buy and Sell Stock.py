 def maxProfit(self, prices: List[int]) -> int:
        
      
   #   TWO POINTER METHOD
  
        l=0
        r=1
        maxprofit=0
        while r<len(prices):
            if prices[l]<prices[r]:                                         # T=O(N)
                profit=prices[r]-prices[l]                                  # S=O(1)
                maxprofit=max(maxprofit,profit)
            else:
                l=r
            r+=1
        return maxprofit
