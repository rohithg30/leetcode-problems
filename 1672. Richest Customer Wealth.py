    def maximumWealth(self, accounts: List[List[int]]) -> int:
    
    #approach 1
        res=[]
        for i in accounts:
            res.append(sum(i))
        return max(res)
        
   
  #approach 2
  
          max_w=0
          for i in accounts:
              c=sum(i)
              max_w=max(max_w,c)
          return max_w
