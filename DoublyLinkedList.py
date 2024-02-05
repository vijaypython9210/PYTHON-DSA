class Node:
    def __init__(self,data):
        self.prev=None
        self.data=data
        self.next=None

class DoublyLinkedList:
    def __init__(self):
        self.head=None

    def display(self):
        if self.head is None:
            print('Empty')
            return
        temp=self.head
        while(temp):
            print(temp.data)
            temp=temp.next
    
    def insertAtBegin(self,data):
        new_Node=Node(data)
        if self.head is None:
            self.head=new_Node
            return
         
        self.head.prev=new_Node
        new_Node.next=self.head
        self.head=new_Node
        return
    
    def deleteAtBegin(self):
        if self.head is None:
            print('Enter a valid Option in LinkedList')
            return
        if self.head.next is not None:
            self.head.next.prev=None
            self.head=self.head.next
            return
        if self.head.next is None and self.head.prev is None:
            self.head=None
            return
        
    def insertAtSpecificPosition(self,pos,value):
        if pos > self.size():
            print('Enter a valid index in LinkedList')
            return
        if pos == 1:
            self.insertAtBegin(value)
            return
        new_Node=Node(value)
        temp=self.head
        for i in range(1,pos):
            temp=temp.next
        prev_Node=temp.prev
        prev_Node.next=new_Node
        new_Node.prev=temp.prev
        temp.prev=new_Node
        new_Node.next=temp
        return
            
    
    def insertAtEnd(self,data):
        new_Node=Node(data)
        if self.head is None:
            self.head=new_Node
            return
        temp=self.head
        while(temp.next):
            temp=temp.next
        temp.next=new_Node
        new_Node.prev=temp
        return
    
    def deleteAtSpecificPosition(self,pos):
        if pos > self.size():
            print('Enter a valid index in LinkedList')
            return
        
        if pos == 1:
            self.deleteAtBegin()
            return
        temp=self.head
        for i in range(1,pos):
            temp=temp.next
        prev_Node=temp.prev
        prev_Node.next=temp.next
        return
    
    def deleteAtEnd(self):
        if self.head is None:
            print('Enter a valid index in LinkedList')
            return
        if self.head.next is None and self.head.prev is None:
            self.head=None
            return
        temp=self.head
        while(temp.next):
            temp=temp.next
        prev_Node=temp.prev
        prev_Node.next=None
        return

    def size(self):
        temp=self.head
        count=0
        while(temp):
            count+=1
            temp=temp.next
        return count
        

if __name__=="__main__":
    dlist=DoublyLinkedList()
    while True:
        option=int(input('Enter a Option:'))
        if option==1:
            value=int(input("Enter a Value:"))
            dlist.insertAtBegin(value)
        elif option==2:
            dlist.deleteAtBegin()
        elif option==3:
            value=int(input("Enter a Value:"))
            pos=int(input("Enter a Position:"))
            dlist.insertAtSpecificPosition(pos,value)
        elif option==4:
            index=int(input("Enter a Position:"))
            dlist.deleteAtSpecificPosition(index)
        elif option==5:
            value=int(input("Enter a Value:"))
            dlist.insertAtEnd(value)
        elif option==6:
            dlist.deleteAtEnd()
        elif option==7:
            dlist.display()
        elif option==8:
            exit(0)
        else:
            print('Enter a valid a Options')
