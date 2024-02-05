class Node:
    def __init__(self,data):
        self.data=data
        self.next=None

class SinglyLinkedList:
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
        
        new_Node.next=self.head
        self.head=new_Node
        return

    def deleteAtBegin(self):
       if self.head is None:
            print('Enter a valid Option in LinkedList')
            return
       self.head=self.head.next
       return

    def insertAtSpecificPosition(self,index,data):
        if index is None or index > self.size():
            print('Enter a valid index in LinkedList')
            return
        if index == 0:
            self.insertAtBegin(data)
            return
        new_Node=Node(data)
        temp=self.head
        for i in range(0,index-1):
            temp=temp.next
        new_Node.next=temp.next
        temp.next=new_Node
        return

    def deleteAtSpecificPosition(self,index):
        if index is None or index > self.size():
            print('Enter a valid index in LinkedList')
            return
        
        if index == 0:
            self.deleteAtBegin()
            return
        temp=self.head
        for i in range(0,index):
            prev=temp
            temp=temp.next
        prev.next=temp.next
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
        return

    def deleteAtEnd(self):
        if self.head is None:
            print('Enter a valid index in LinkedList')
            return
        
        temp=self.head
        while(temp.next):
            prev=temp
            temp=temp.next
        prev.next=None

    def search(self,value):
        temp=self.head
        while temp:
            if temp.data==value:
                return "Yes"
            else:
                temp=temp.next
        return "No"
    
    def reverse(self):
        if self.head is None:
            print('Enter a valid index in LinkedList')
            return
        
        temp=self.head
        prev=None
        while temp:
            next=temp.next
            temp.next=prev
            prev=temp
            temp=next
        self.head=prev
        self.display()
        return

    def size(self):
        temp=self.head
        count=0
        while(temp):
            count+=1
            temp=temp.next
        return count


if __name__=='__main__':
    llist=SinglyLinkedList()
    while True:
        option=int(input('Enter a Option:'))
        if option==1:
            value=int(input("Enter a Value:"))
            llist.insertAtBegin(value)
        elif option==2:
            llist.deleteAtBegin()
        elif option==3:
            value=int(input("Enter a Value:"))
            index=int(input("Enter a Position:"))
            llist.insertAtSpecificPosition(index,value)
        elif option==4:
            index=int(input("Enter a Position:"))
            llist.deleteAtSpecificPosition(index)
        elif option==5:
            value=int(input("Enter a Value:"))
            llist.insertAtEnd(value)
        elif option==6:
            llist.deleteAtEnd()
        elif option==7:
            llist.display()
        elif option==8:
            exit(0)
        elif option==9:
            value=int(input("Enter a Value:"))
            print(llist.search(value))
        elif option==10:
            llist.reverse()
        else:
            print('Enter a valid a Options')

    