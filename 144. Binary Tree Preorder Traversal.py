class Solution:
 
# Recursive Approach [ T-->O(N),S-->O(N) ]
     def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        
        res=[]
        if root==None:
            return res
        def recu(node):
            res.append(node.val)
            if node.left:
                recu(node.left)
            if node.right:
                recu(node.right)
        recu(root)
        return res
                
 # Iteration Approach [ T-->O(N),S-->O(N) ]
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        
        
        if not root:
            return []
        res=[]
        stack=[]
        stack.append(root)
        while stack:
            node=stack.pop()
            res.append(node.val)
            if node.right:
                stack.append(node.right)
            if node.left:
                stack.append(node.left)
        return res
                
# Morris Traversal Approach [ T-->O(N),S-->O(1) ] BEST-->
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        
        res=[]
        if not root:
            return res
        cur=root
        while cur:
            res.append(cur.val)
            if cur.left:
                pre=cur.left
                while pre.right:
                        pre=pre.right
                if pre.right==None:
                    pre.right=cur.right
                    cur=cur.left
            else:
                cur=cur.right
        return res
                    
