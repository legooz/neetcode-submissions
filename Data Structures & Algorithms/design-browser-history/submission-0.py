class Node:
    def __init__(self, page: str):
        self.next = None
        self.prev = None
        self.page = page


class BrowserHistory:

    def __init__(self, homepage: str):
        self.cur = Node(homepage)
        
    def visit(self, url: str) -> None:
        new_site = Node(url)
        self.cur.next = new_site
        new_site.prev = self.cur
        self.cur = new_site
        

    def back(self, steps: int) -> str:
        
        for _ in range(steps):
            if self.cur.prev is None:
                return self.cur.page
            self.cur = self.cur.prev
        return self.cur.page

    def forward(self, steps: int) -> str:
        
        for _ in range(steps):
            if self.cur.next is None:
                return self.cur.page
            self.cur = self.cur.next
        return self.cur.page

# Your BrowserHistory object will be instantiated and called as such:
# obj = BrowserHistory(homepage)
# obj.visit(url)
# param_2 = obj.back(steps)
# param_3 = obj.forward(steps)