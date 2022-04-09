
# Solution 1:

# using mod of 2 which get last value and use right shift to remove last value
class Solution:
    def hammingWeight(self, n: int) -> int:
      
      res=0
      while n!=0:                                                 # T---> O(1)[because its is 32bit we know ]
        res+=n%2                                                  # S---> O(1)
        n=n>>1
     return res
  
  
# solution 2:  

# using AND  n AND 1 .  AND operator which both value is 1 then 1 else 0  
class Solution:
    def hammingWeight(self, n: int) -> int:
      
      res=0
      for i in  range(32):                                              # T-----> O(1)
        if n&1==1:                                                      # S----> O(1)
          res+=1
        n=n>>1
      return res
  
