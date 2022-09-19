class Solution:
  
  # T--> O(N)+O(N) [grid traverese +BFS traverse] S---> O(N)+O(N) [queue space + vis(list) space + recursive space ]
    def numIslands(self, grid: List[List[str]]) -> int:
        
        vis=[[0 for _ in range(len(grid[0]))]for _ in range(len(grid))]
        res=0
        for row in range(len(grid)):
            for col in range(len(grid[0])):
                if grid[row][col]=="1" and vis[row][col]==0:
                    self.bfs(grid,row,col,vis)
                    res+=1
        return res
    
    def bfs(self,grid,row,col,vis):
        
        que=[]
        que.append([row,col])
        while que:
            i,j=que.pop(0)
            if vis[i][j]==0:
                vis[i][j]=1
                if i+1<len(grid) and grid[i+1][j]=="1":
                    que.append([i+1,j])
                if i>0 and grid[i-1][j]=="1":
                    que.append([i-1,j])
                if j>0 and grid[i][j-1]=="1":
                    que.append([i,j-1])
                if  j+1<len(grid[0])and grid[i][j+1]=="1":
                    que.append([i,j+1])
        
            
        
