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
            return ele
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

def preced(ch):
    if ch=="+" or ch=="-":
        return 1
    elif ch=="*" or ch=="/":
        return 2
    elif ch=="^":
        return 3
    else:
        return 0

def Postfix(exp):
    # Operators = set(['+', '-', '*', '/', '(', ')', '^'])
    st = Stack(30)
    postfix=""
    for item in exp:
        if(item.isalpha()):
           postfix+=item
        elif item=="(":
            st.Push(item)
        elif item=="^":
            st.Push(item)
        elif item==")":
            while st.isEmpty()==False and st.Peak()!="(":
                ch = st.Pop()
                postfix+=ch
            st.Pop()
        else:
            while st.isEmpty()==False and preced(item)<=preced(st.Peak()):
                ch=st.Pop()
                postfix+=ch
            st.Push(item)
    while(st.isEmpty()!=True):
           ch=st.Pop()
           postfix+=ch
    return postfix

exp = "a+b-(a-b*c)+k"
print(Postfix(exp))
                

        



