class Node:
    def __init__(self, key, val):
        self.key = key
        self.val = val
        self.next = None
        self.prev = None

class LRUCache:

    def __init__(self, capacity: int):
        self.cap = capacity
        self.hashMap = {}
        self.left = Node(None,None)
        self.right = Node(None,None)
        self.left.next = self.right
        self.right.prev = self.left
    def add(self, node):
        prev = self.right.prev
        nxt = self.right
        prev.next = node
        nxt.prev = node
        node.next = nxt
        node.prev = prev

    def remove(self, node):
        lft = node.prev
        nxt = node.next
        lft.next = nxt
        nxt.prev = lft

        

    def get(self, key: int) -> int:
        if key in self.hashMap:
            self.remove(self.hashMap[key])
            self.add(self.hashMap[key])
            return self.hashMap[key].val
        return -1
        
        

    def put(self, key: int, value: int) -> None:
        if key in self.hashMap:
            self.remove(self.hashMap[key])
        newNode = Node(key,value)
        self.hashMap[key]=newNode
        self.add(newNode)

        if len(self.hashMap) > self.cap:
            next_lru = self.left.next
            self.remove(next_lru)
            del self.hashMap[next_lru.key]
        

        


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)