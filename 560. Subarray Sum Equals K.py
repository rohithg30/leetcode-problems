   def subarraySum(self, nums: List[int], k: int) -> int:
    
    # BRUTE FORCE APPROACH      // O(n^2)    
        count=0
        for i in range(len(nums)):
            for  j in range(i,len(nums)):
                if sum(nums[i:j+1])==k:
                    count+=1
        return count
                    
       
     # BETTER SOLUTION          // O(N)
        count=0
        curr=0
        hashm={0:1}
        for i in range(len(nums)):
            curr+=nums[i]
            if curr-k in hashm:
                count+=hashm[curr-k]
            if curr in hashm:
                hashm[curr]+=1
            else:
                hashm[curr]=1
        return count
        
