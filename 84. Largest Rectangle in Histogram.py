    def largestRectangleArea(self, heights: List[int]) -> int:
    
    # bruteforce (O(N^2))
    
    
        maxarea=0
        for i in range(len(heights)):
            minheight=heights[i]
            for j in range(i,len(heights)):
                minheight=min(minheight,heights[j])
                curarea=(j-i+1)*minheight
                maxarea=max(curarea,maxarea)
        return maxarea
      
      
      #optimise (O(N))
      
        n=len(heights)
        left=[None]*n
        right=[None]*n
        stack=[]
        for i in range(n):
            while stack and heights[i]<=heights[stack[-1]]:
                stack.pop()
            if not stack:
                left[i]=0
            else:
                left[i]=stack[-1]+1
            stack.append(i)

        stack.clear()
        for i in range(n)[::-1]:
            while stack and heights[i]<=heights[stack[-1]]:
                stack.pop()
            if not stack:
                right[i]=n-1
            else:
                right[i]=stack[-1]-1
            stack.append(i)
        maxarea=0
        for i in range(n):
            maxarea=max(maxarea,heights[i]*(right[i]-left[i]+1))
        return maxarea

