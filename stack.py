class stack_list:
    def __init__(self):
        self_stack = []

    def push(self, data):
        self.stack.append(data)
        print(f"Pushed {data} into stack")

    def size(self):
        return len(self.stack)       

    def top(self):
        if self.is_empty():
            print("Stack is empty in top")
            return None
        return self.stack([-1])
    
    def pop(self):
        if self.is_empty():
            print("Stack is empty to pop")
            return None
        return self.stack.pop()