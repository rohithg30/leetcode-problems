# BINARY SEARCH 

class Solution:
    def findMin(self, nums: List[int]) -> int:
        
        res=nums[0]
        left=0
        right=len(nums)-1                                                           # O(log N) ----> TIME COMPLEXITY
        while left<=right:                                                          #  O(1) ---> SPACE COMPLEXITY
            if nums[left]<nums[right]:
                res=min(res,nums[left])
                break
            mid=(left+right)//2
            res=min(res,nums[mid])
            if nums[mid]>=nums[left]:
                left=mid+1
            else:
                right=mid-1
        return res
      
      
      
      --------------------------------------------------------------------------------
      
      # python min function return minium value
      
    class Solution:
        def findMin(self, nums: List[int]) -> int:
                return min(nums)                                                       # O(N) ---> TIME COMPLEXITY
                                                                                        # O(1) --> SPACE COMPLEXITY
