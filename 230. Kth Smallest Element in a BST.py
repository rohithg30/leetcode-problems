class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        
        # Recrsion Approach [T-->O(N)+NlogN ,S-->O(N)+O(N)-->auxspace+list space]
        self.ls=[]
        def dfs(node):
            if node==None:
                return 
            self.ls.append(node.val)
            dfs(node.left)
            dfs(node.right)
        dfs(root)
        self.ls.sort()
        return self.ls[k-1]
      
      # Recursion Approach [T--->O(N),S-->O(N)--> aux space]
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        
        
        self.ksmall=None
        self.count=1
        def dfs(node):
            if not node or self.ksmall:
                return 
            dfs(node.left)
            if self.count==k:
                self.ksmall=node.val
            self.count+=1
            dfs(node.right)
        dfs(root)
        return self.ksmall
    
    # Stack Approach [T-->O(N) ,S--->O(N)]
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        
        stack=[]
        while True:
            while root:
                stack.append(root)
                root=root.left
            root=stack.pop()
            k-=1
            if not k:
                return root.val
            root=root.right
     
    # Morris Traversal Approach [T-->O(N),S-->O(1)] ---> BEST
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        
        res=None
        cur=root
        count=0
        while cur:
            if cur.left:
                prev=cur.left
                while prev.right:
                    prev=prev.right
                tmp=cur.left
                prev.right=cur
                cur.left=None
                cur=tmp
            else:
                count+=1
                if count==k:
                    return cur.val
                cur=cur.right
                
            
        
        
