class Solution:
  
  # Recursion Aprroach [ T-->O(N), S-->O(N) ]
  def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        
        self.res=[]
        if not root:
            return self.res
        def inorder(node):
            if node.left:
                inorder(node.left)
            self.res.append(node.val)
            if node.right:
                inorder(node.right)
        inorder(root)
        return self.res
      
  # Iterative Approach [ T-->O(N),S--->O(N) ]
  def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
    
        res=[]
        if not root:
            return res
        stack=[]
        while True:
            if root:
                stack.append(root)
                root=root.left
            else:
                if not stack:
                    break
                root=stack.pop()
                res.append(root.val)
                root=root.right
        return res
        
            
  # (Morris Traversal Approach [ T-->O(N) , S---> O(1) ] ---> BEST
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        
        res=[]
        if not root:
            return res
        cur=root
        while cur:
            if cur.left==None:
                res.append(cur.val)
                cur=cur.right
            else:
                pre=cur.left
                while pre.right and pre.right!=cur:
                    pre=pre.right
                if pre.right==None:
                    pre.right=cur
                    cur=cur.left
                else:
                    pre.right=None
                    res.append(cur.val)
                    cur=cur.right
        return res
        
