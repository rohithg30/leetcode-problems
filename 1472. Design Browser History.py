 # APPROACH 1 ..
# USING LIST METHOD []
# T--->O(N),S--->O(N)
     
class BrowserHistory:

    def __init__(self, homepage: str):
        
        self.history=[homepage]
        self.pointer=0
        
  
        

    def visit(self, url: str) -> None:
        
        while len(self.history)-1>self.pointer:
            self.history.pop()
        self.history.append(url)
        self.pointer+=1
  

    def back(self, steps: int) -> str:
        
        while self.pointer>0 and steps>0:
            self.pointer-=1
            steps-=1
        return self.history[self.pointer]
        
    def forward(self, steps: int) -> str:
        
        while len(self.history)-1>self.pointer and steps>0:
            steps-=1
            self.pointer+=1
        return self.history[self.pointer]
 
#  APPROACH 2 ..
        
 # USING LINKED LIST [O--->O-->]
# T--->O(N),S--->O(N)

class newnode:
    def __init__(self,val):
        self.val=val
        self.prev=None
        self.next=None
class BrowserHistory:

    def __init__(self, homepage: str):
        
        self.head=newnode(homepage)
        
    def visit(self, url: str) -> None:
        node=newnode(url)
        node.prev=self.head
        self.head.next=node
        self.head=node

    def back(self, steps: int) -> str:
        
        while self.head.prev and steps:
            self.head=self.head.prev
            steps-=1
        return self.head.val

    def forward(self, steps: int) -> str:
        
        while self.head.next and steps:
            self.head=self.head.next
            steps-=1
        return self.head.val


   
