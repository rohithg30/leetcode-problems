class Node:
    def __init__(self,key,val):
        self.key=key
        self.val=val
        self.next=None
        self.prev=None
class LRUCache:

    def __init__(self, capacity: int):
        
        self.cap=capacity
        self.cache={}
        self.head=Node(0,0)
        self.tail=Node(0,0)
        self.head.next=self.tail
        self.tail.prev=self.head
        
    def remove(self,node):
        node.prev.next=node.next
        node.next.prev=node.prev
        
        
    def insert(self,node):
        headnext=self.head.next
        self.head.next=node
        node.prev=self.head
        node.next=headnext
        headnext.prev=node

    def get(self, key: int) -> int:
        
        if key in self.cache:
            self.remove(self.cache[key])
            self.insert(self.cache[key])
            return self.cache[key].val
        return -1

    def put(self, key: int, value: int) -> None:
        
        if key in self.cache:
            self.remove(self.cache[key])
        self.cache[key]=Node(key,value)
        self.insert(self.cache[key])
        
        if len(self.cache)>self.cap:
            lru=self.tail.prev
            self.remove(lru)
            del(self.cache[lru.key])
        
