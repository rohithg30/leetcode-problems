class Solution:
    def validateStackSequences(self, pushed: List[int], popped: List[int]) -> bool:
        
        stack=[]
        i=0
        for  num in pushed:
            stack.append(num)
            while stack and i<len(popped) and stack[-1]==popped[i]:
                stack.pop()
                i+=1
        return i==len(pushed)
      
      
      # T---> O(N)
      # S---> O(N)
    
 
class Solution:
    def validateStackSequences(self, pushed: List[int], popped: List[int]) -> bool:
        
        i=0
        while i<len(pushed) and pushed:
            if pushed[i]==popped[0]:
                popped.pop(0)
                pushed.pop(i)
                i=max(i-1,0)
            else:
                i+=1
        return True if not pushed else False
    
            # T--> O(N)
            # S--> O(1)
                
