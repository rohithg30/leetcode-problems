class Solution:
  
  #  DFS --->
  # T-->O(N) S-->O(N)[recursive space]
  
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        
        lenr=len(image)
        lenc=len(image[0])
        oldcolor=image[sr][sc]
        img=image.copy()
        if oldcolor==color:
            return img
        def dfs(row,col):
            if img[row][col]==oldcolor:
                img[row][col]=color
                if row>=1:dfs(row-1,col)
                if row+1<lenr:dfs(row+1,col)
                if col>=1:dfs(row,col-1)
                if col+1<lenc:dfs(row,col+1)
        dfs(sr,sc)
        return img
     
    
    # BFS -->
    # T---> O(N) ,S-->O(N)+O(N)+O(N) [queue+visited,recursive]
    
     def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        
        
        def bfs(image,sr,sc,vis,old,color):
            que=[]
            que.append([sr,sc])
            while que:
                #print(que)
                row,col=que.pop(0)
                #print(row)
                #print(col)
                if vis[row][col]==0 and image[row][col]==old:
                    vis[row][col]=1
                    image[row][col]=color
                    if (row-1 >=0) and  image[row-1][col]==old:
                        que.append([row-1,col])
                    if row+1 < len(image) and  image[row+1][col]==old:
                        que.append([row+1,col]) 
                    if col-1>=0 and image[row][col-1]==old:
                        que.append([row,col-1])
                    if col+1<len(image[0]) and image[row][col+1]==old:
                        que.append([row,col+1])
        vis=[[0 for _ in range(len(image[0]))]for _ in range(len(image))]
        bfs(image,sr,sc,vis,image[sr][sc],color)
        return image
