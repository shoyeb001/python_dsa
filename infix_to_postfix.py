class Stack:
    def __init__(self,max_size):
        self.top=-1
        self.max = max_size
        self.arr = [None]*max_size
    def isEmpty(self):
        if self.top==-1:
           return True
        else:
            return False
    def isFull(self):
        if self.top==self.max:
            return True
        else:
            return False
    def Push(self,ele):
        if self.isFull():
            print("Stack is full")
        else:
            self.top = self.top+1
            self.arr[self.top] = ele
    def Pop(self):
        if self.isEmpty():
            print("Stack Underflow")
        else:
            ele = self.arr[self.top]
            self.arr[self.top]=None
            self.top = self.top-1
    def Display(self):
        if self.isEmpty():
            print("stack is empty")
        else:
            for i in range(self.top,-1,-1):
                print(self.arr[i])
    def Peak(self):
        if self.isEmpty():
            print("Stack is Empty")
        else:
            return self.arr[self.top]

buck = stack()

character = ab+cd+(v-j)
exp=""
for i in character:
    


