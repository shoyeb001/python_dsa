class Node:
    def __init__(self,data):
        self.data = data
        self.prev = None
        self.next = None
class LinkedList:
    def __init__(self):
        self.head=None
        
    def traverse(self):
        if(self.head==None):
            print("Linked List is empty")
        else:
            n=self.head
            while(n.next==None):
                print(n.data)
                n = n.next
    

link = LinkedList()
LinkedList.traverse()
