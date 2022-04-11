# solution 1:

# looping and check i in list or not 

class Solution:
    def missingNumber(self, nums: List[int]) -> int:
      
      for i in range(len(nums)+1):                        # T---> O(N)
        if i not in nums:                                 # S---> O(1)
          return i
        
# solution 2:

# multiply len(nums) with len(nums)+1 and divide by 2 and subtract with sum(nums)

class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        
        n=len(nums)
        res=n*(n+1)//2 -sum(nums)                         # T----> O(N)
        return res                                        # S----> O(1)
      
 # solution 3: 


class Solution:
    def missingNumber(self, nums: List[int]) -> int:
      
      res=len(nums)         
      for i in range(len(nums)):                              # T---> O(N)
         res+=(i-nums[i])                                     # S---> O(1)
      return res
        
      
      
