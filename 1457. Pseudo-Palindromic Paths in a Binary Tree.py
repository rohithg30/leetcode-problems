class Solution:
  
  # T--->O(N^2) [list*dictionary traverse] ,s-->O(2N) [list +dictionary] 
   
    ----> # TLE or MLE
  
    def pseudoPalindromicPaths (self, root: Optional[TreeNode]) -> int:
        
        self.ans=[]
        def preorder(node,ds):
            if not node:
                return 
            ds.append(node.val)
            if not node.left and not node.right:
                self.ans.append(ds.copy())
                ds.pop()
                return
            preorder(node.left,ds)
            preorder(node.right,ds)
            ds.pop()
        preorder(root,[])
        

        res=0
        for i in self.ans:
            count=Counter(i)
            odd=0
            for i in count.values():
                if i%2!=0:
                    odd+=1
            if odd<=1:
                res+=1
        return res
      
      
-----------------------------------------------------------------------------------------------

# T---O(N),S--->O(N) [ dictionary space]

   def pseudoPalindromicPaths (self, root: Optional[TreeNode]) -> int:
        
        def checkpalindrome(d):         # Check can we make palidrome or not 
            oddno=0
            for i in d.values():
                if i%2!=0:
                    oddno+=1
            if oddno>1:
                return False
            return True
        
        
        self.res=0                          # Final answer 
        
        
        def preorder(node,dic):                           #  Traverse tree and  count node values how many times appear 
            if node:
                dic[node.val]+=1
                if not node.left and not node.right:
                    if checkpalindrome(dic):                # check if palindrome
                        self.res+=1
                        dic[node.val]-=1
                        return
                preorder(node.left,dic)
                preorder(node.right,dic)
                dic[node.val]-=1
        preorder(root,defaultdict(int))
        
        return self.res
            
        
