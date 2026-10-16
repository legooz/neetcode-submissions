class Node:
    def __init__(self, val):
        self.val = val
        self.next = None
        self.prev = None
        

class MyLinkedList:

    def __init__(self):
        self.left = Node(0)
        self.right = Node(0)
        self.left.next = self.right
        self.right.prev = self.left
        self.size = 0
    def get(self, index: int) -> int:
        count = 0
        current = self.left.next
      
        while current is not self.right and count < index:
            current = current.next
            count += 1
        if current is self.right:
            return -1
        return current.val
   

    def addAtHead(self, val: int) -> None:
        prev = self.left #set prev as the sentinel node (left-most)
        new = prev.next #set to prev.next so the sentinel pointer is not lost 
        node = Node(val) # create the new node
        node.prev = prev # point the new node at the sentinel node
        node.next = new # add the node next pointer to prev.next
        prev.next = node # add the prev next pointer to node so sentinel points at it
        new.prev = node # point the node to the right of the added back towards it
        self.size += 1
        

    def addAtTail(self, val: int) -> None:
        right_next = self.right # set right next as sentinel node (right-most)
        new = right_next.prev # keep the pointer
        node = Node(val) # create new node
        node.next = right_next # set the node right pointer to the right sentinel
        node.prev = new # set the node pointer to the previous node
        right_next.prev = node # set the right-sentinel node prev pointer to the node
        new.next = node # set the old-tail next pointer to the added node
        self.size += 1
    def addAtIndex(self, index: int, val: int) -> None:
        if index > self.size:         
            return
        prev = self.left
        for _ in range(index):
            prev = prev.next
        new = prev.next
        node = Node(val)
        node.prev = prev
        node.next = new
        prev.next = node
        new.prev = node
        self.size += 1

    def deleteAtIndex(self, index: int) -> None:
        if index >= self.size:      
            return
        prev = self.left
        for _ in range(index):
            prev = prev.next
        current = prev.next
        new  = current.next
        prev.next = new
        new.prev = prev
        self.size -= 1

# Your MyLinkedList object will be instantiated and called as such:
# obj = MyLinkedList()
# param_1 = obj.get(index)
# obj.addAtHead(val)
# obj.addAtTail(val)
# obj.addAtIndex(index,val)
# obj.deleteAtIndex(index)