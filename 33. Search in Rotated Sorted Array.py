# BINARY SEARCH ALGORITHM 

class Solution:
    def search(self, nums: List[int], target: int) -> int:
        
        left=0
        right=len(nums)-1
        while left<=right:                                                          # O(logN) ---> TIME COMPLEXITY
            mid=(left+right)//2                                                     # O(1) ---> SPACE COMPLEXITY 
            if nums[mid]==target:   
                return mid
            
            if nums[left]<=nums[mid]:
                if target>nums[mid] or target<nums[left]:
                    left=mid+1
                else:
                    right=mid-1
            else:
                if target<nums[mid] or target>nums[right]:
                    right=mid-1
                else:
                    left=mid+1
        return -1
      
-----------------------------------------------------------------------------------------------> 

 # LINERAR SEARCH ALGORITHM     

class Solution:
    def search(self, nums: List[int], target: int) -> int:
      
       for i in range(len(nums)):                                                       # O(N) ----> TIME COMPLEXITY  
          if nums[i]==target:                                                           # O(1) ----> SPACE COMPLEXITY
            return i
       return -1
    
        
      
