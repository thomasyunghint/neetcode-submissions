class MinStack:

    def __init__(self):
        self.stack = []
        self.MinStack=[]
        

    def push(self, val: int) -> None:
        self.stack.append(val)
        val_min = min(val, self.MinStack[-1] if self.MinStack else val)
        self.MinStack.append(val_min)

    def pop(self) -> None:
        self.stack.pop()
        self.MinStack.pop()

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.MinStack[-1]