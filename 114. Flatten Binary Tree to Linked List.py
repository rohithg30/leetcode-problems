# Recursive method 

# T---> O(N)
# S---> O(H) [ H ---> height of tree ] 
class Solution:
    def flatten(self, root: Optional[TreeNode]) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        
        def dfs(root):
            
            if not root:
                return None
            lefttail=dfs(root.left)
            righttail=dfs(root.right)
            if root.left:
                lefttail.right=root.right
                root.right=root.left
                root.left=None
            
            last= righttail or lefttail or root
            return last
        dfs(root)
    
    
 # using stack method 

# T---> O(N)
# S---> O(N)


class Solution:
    def flatten(self, root: Optional[TreeNode]) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        if not  root:
            return None
        st=[root]
        while st:
            cur=st[-1]
            st.pop()
            if cur.right:
                st.append(cur.right)
            if cur.left:
                st.append(cur.left)
            if st:
                cur.right=st[-1]
            cur.left=None

# Best solution

# T--->O(N)
# S--->O(1)
            
class Solution:
    def flatten(self, root: Optional[TreeNode]) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        if not root:
            return None
        cur=root
        while cur:
            if cur.left:
                prev=cur.left
                while prev.right:
                    prev=prev.right
                prev.right=cur.right
                cur.right=cur.left
                cur.left=None
            cur=cur.right
        
