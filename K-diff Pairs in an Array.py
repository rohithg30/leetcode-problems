  def findPairs(self, nums: List[int], k: int) -> int:
        
        count=0
        d=Counter(nums)
        
        if k==0:
            for i,v in d.items():
                if v>1:
                    count+=1
        else:
            for i in d.keys():
                if i+k in nums:
                    count+=1
                    
        return count
