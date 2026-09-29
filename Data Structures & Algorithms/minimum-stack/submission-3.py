class MinStack:

    def __init__(self):
        self.array = []
        self.min_vals = []
        
    def push(self, val: int) -> None:
        if not self.array:
            self.min_vals.append(val)

        if self.array:
            if val <= self.min_vals[-1]:
                self.min_vals.append(val)
        
        self.array.append(val)

    def pop(self) -> None:
        if self.min_vals[-1] == self.array[-1]:
            self.min_vals.pop()

        self.array.pop()

    def top(self) -> int:
        return self.array[-1]

    def getMin(self) -> int: 
        return self.min_vals[-1]
