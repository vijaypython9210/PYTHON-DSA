class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
class Queue:
    def __init__(self):
        self.front=None
        self.rear=None
    
    def enqueue(self,data):
        new_Node=Node(data)
        if self.front is None:
            self.front=new_Node
            return
        if self.rear is None:
            self.front.next=new_Node
            self.rear=new_Node
            return
        self.rear.next=new_Node
        self.rear=new_Node
        return
        
    def display(self):
        if self.front is None:
            print('List is Empty')
            return
        temp=self.front
        while(temp):
            print(temp.data)
            temp=temp.next
        return

    def dequeue(self):
        if self.front is None:
            print("OOPS list is empty... enter a correct option")
            return
        self.front=self.front.next
        if self.front is None:
            self.rear=None
        return
    
    def isEmpty(self):
        return self.front is None
    
    def peekFront(self):
        if self.front is None:
            print('List is Empty')
            return
        return self.front.data

if __name__=="__main__":
    queue=Queue()
    queue.enqueue(1)
    queue.enqueue(2)
    queue.enqueue(3)
    queue.dequeue()
    print(queue.isEmpty())
    print(queue.peekFront())
    queue.display()