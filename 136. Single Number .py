class Solution:
    def singleNumber(self, nums: List[int]) -> int:
      
      dic={}
      for num in nums:
        if num not in dic:
          dic[num]=1
        else:
          dic[num]+=1
          
     for i in nums:
      if dic[i]==1:
        return i
      
