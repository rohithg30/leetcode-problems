# iterating 
class Solution:
    def connect(self, root: 'Optional[Node]') -> 'Optional[Node]':
        
        if not root:
            return None
        cur,nxt=root,root.left
        while cur and nxt:
            cur.left.next=cur.right
            if cur.next:
                cur.right.next=cur.next.left
            cur=cur.next
            if not cur:
                cur=nxt
                nxt=cur.left
        return root




# usign queue 

class Solution:
    def connect(self, root: 'Optional[Node]') -> 'Optional[Node]':
        
        if not root:
            return None
        queue=[root]
        while queue:
            cur=queue.pop(0)
            if cur.left and cur.right:
                cur.left.next=cur.right
                if cur.next:
                    cur.right.next=cur.next.left
                queue.append(cur.left)
                queue.append(cur.right)
        return root
      
      
# using Stack


class Solution:
    def connect(self, root: 'Optional[Node]') -> 'Optional[Node]':
        
        if not root:
            return None
        stack=[root]
        while stack:
            cur=stack.pop()
            if cur.left and cur.right:
                cur.left.next=cur.right
                if cur.next:
                    cur.right.next=cur.next.left
                stack.append(cur.right)
                stack.append(cur.left)
        return root      
