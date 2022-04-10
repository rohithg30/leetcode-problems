# USING STACK 

class Solution:
    def calPoints(self, ops: List[str]) -> int:
        
        stack=[]
        for op in ops:
            if op=="C":                                                 # T---> O(N)
                stack.pop()                                             # S---> O(N)
            elif op=="D": 
                stack.append(stack[-1]*2)
            elif op=="+":
                stack.append(stack[-1]+stack[-2])
            else:
                stack.append(int(op))
        return sum(stack)
