# using dummy node


# T--->O(N) 
# S--->O(1)

class Solution:
    def connect(self, root: 'node') -> 'Node':

        if not root:
            return None
        tail = dummy = Node(0)
        res=root
        while root:
            tail.next = root.left
            if tail.next:
                tail = tail.next
            tail.next =root.right
            if tail.next:
                tail = tail.next
            root = root.next
            if not root:
                tail = dummy
                root = dummy.next
        return res
      
      
#  using Queue data structure 

# T--->O(N)
# S---->O(1)

class Solution:
    def connect(self, root: 'Node') -> 'Node':
        
        if not root:
            return root
        que=[]
        que.append(root)
        tail=root
        while len(que)>0:
            n=que.pop(0)
            if n.left:
                que.append(n.left)
            if n.right:
                que.append(n.right)
            if n==tail:
                n.next=None
                tail=que[-1] if len(que)>0 else None
            else:
                n.next=que[0]
        return root
