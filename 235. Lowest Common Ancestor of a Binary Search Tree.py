class Solution:
  
  # Recursive Approach [T-->O(N),S--->O(N) (aux space considered) ]
  
      def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        

          def dfs(node):
              if not node:
                  return None
              if node.val<p.val and node.val<q.val:
                  return dfs(node.right)
              if node.val>p.val and node.val>q.val:
                  return dfs(node.left)
              return node
          return dfs(root)
    
  # Iteration Approach [T--> O(N),S--->O(1)]
  
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
      
        cur=root
        while cur:
            if cur.val<p.val and cur.val<q.val:
                cur=cur.right
            elif cur.val>p.val and cur.val>q.val:
                cur=cur.left
            else:
                return cur
        
            
        
