# BRUTE FROCE 

#  O(N^2)---->T
#  O(N)---->S

class Solution:
    def maxArea(self, height: List[int]) -> int:
      res=0
      for i in range(len(height)):
        for j in range(i+1,len(height)):
          area=(j-i)*min(height[i],height[j])
          res=max(res,area)
      return res
    
    
    # BEST SOLITION 
    # O(N)---->T
    # O(N)--->S
    
         res=0
         l=0
         r=len(height)-1
         while l<r:
            area=(r-l)*min(height[l],height[r])
            res=max(res,area)
            if height[l]<heigth[r]:
              l+=1
            elif height[r]<height[l]:
              r-=1
            else:
              l+=1
        return res
                     
     
