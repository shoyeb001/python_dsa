class Node:
    def __init__(self,data):
        self.data=data
        self.ref=None
class LinkedList:
    def __init__(self):
        self.head=None
    def traverse(self):
        if self.head==None:
            print("LinkedList is empty")
        else:
            n = self.head
            while(n!=None):
                print(n.data)
                n=n.ref
    def add_begin(self,data):
        new_node = Node(data)
        new_node.ref = self.head
        self.head = new_node
    def add_end(self,data):
        new_node = Node(data)
        if self.head==None:
            print("Linked List is empty")
        else:
            n = self.head
            while n.ref!=None:
                n = n.ref
            n.ref = new_node
    def ad_between(self,data,position):
        new_node = Node(data)
        n = self.head
        while(n.ref!=None):
            if(position==n.data):
                break
            n = n.ref
        new_node.ref=n.ref
        n.ref=new_node
    def delete_begining(self):
        if self.head == None:
            print("Linkedlist is empty")
        else:
            self.head = self.head.ref
    def delete_end(self):
        if self.head == None:
            print("Linkedlist is empty")
        else:
            n= self.head
            while(n.ref.ref!=None):
                n=n.ref
            n.ref=None
    def delete_by_data(self,x):
        if self.head == None:
            print("Linkedlist is empty")
        elif self.head.data==x:
            self.head = self.head.ref
        else:
            n = self.head
            while(n.ref!=None):
                if n.ref.data==x:
                    n.ref = n.ref.ref
                n=n.ref
link = LinkedList()
link.add_begin(20)
link.add_begin(10)
link.ad_between(50,20)
link.add_end(30)
# link.traverse()
# link.delete_begining()
# link.delete_end()
# link.traverse()
link.delete_by_data(50)
link.traverse()
