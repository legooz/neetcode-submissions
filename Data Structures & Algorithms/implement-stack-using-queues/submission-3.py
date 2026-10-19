class Node:
    def __init__(self, val: int):
        self.val = val
        self.next = None

class MyStack:

    def __init__(self):
        self.tail = None
        self.size = 0
        self.head = None

    def push(self, x: int) -> None:

        if self.size == 0:
            self.head = Node(x)

        else:
            cur = self.head
            while cur.next is not None:
                cur = cur.next
            cur.next = Node(x)
        self.tail = x
        self.size += 1

    def pop(self) -> int:
        if self.head.next is None:
            val = self.head.val
            self.head = self.tail = None
            self.size = 0
            return val

        cur = self.head
        while cur.next.next is not None:
            cur = cur.next

        val = cur.next.val
        self.size -= 1
        cur.next = None
        self.tail = cur.val
        return val

    def top(self) -> int:
        return self.tail

    def empty(self) -> bool:
        if self.head == None:
            return True
        return False



# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()