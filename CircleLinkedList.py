class Node:
    def __init__(self,data):
        self.data=data
        self.next=None

class SingleCircularLinkedList:
    def __init__(self):
        self.last=None

    def display(self):
        if self.last is None:
            print('Empty')
            return
        
        temp=self.last.next
        while(temp is not self.last):
            print(temp.data)
            temp=temp.next
        print(temp.data)
        return

    def insertAtBegin(self,data):
        new_Node=Node(data)
        if self.last is None:
            new_Node.next=new_Node
            self.last=new_Node
            return
        
        new_Node.next=self.last.next
        self.last.next=new_Node
        last=new_Node
        return
    
    def deleteAtBegin(self):
        if self.last is None:
            print('List is Empty')
            return
        elif self.last.next is self.last:
            self.last=None
            return
        else:
            temp=self.last.next
            self.last.next=temp.next
            return
    
    def insertAtEnd(self,data):
        new_Node=Node(data)
        if self.last is None:
            new_Node.next=new_Node
            self.last=new_Node
            return
        
        new_Node.next=self.last.next
        self.last.next=new_Node
        self.last=new_Node
        return
    
    def deleteAtEnd(self):
        if self.last is None:
            print('List is Empty')
            return
        elif self.last.next is self.last:
            self.last=None
            return
        else:
            temp=self.last.next
            temp2=self.last.next
            while(temp.next is not self.last):
                temp=temp.next
            temp.next=temp2
            self.last=temp
            return
    
    def insertAtSpecificPosition(self,pos,data):
        if pos is None or pos > self.size():
            print('Enter a valid index in CirclarList')
            return
        if pos == 1:
            self.insertAtBegin(data)
            return
        
        new_Node=Node(data)
        temp=self.last
        for i in range(1,pos):
            temp=temp.next
        new_Node.next=temp.next
        temp.next=new_Node
        return
    
    def deleteAtSpecificPosition(self,pos):
        if  pos > self.size():
            print('Enter a valid index in LinkedList')
            return
        
        elif pos == 1:
            self.deleteAtBegin()
            return
        
        temp=self.last
        for i in range(1,pos+1):
            prev=temp
            temp=temp.next
        prev.next=temp.next
        return
    
    def size(self):
        if self.last is None:
            return 0
        temp=self.last.next
        count=0
        while(temp is not self.last):
            count+=1
            temp=temp.next
        return count
    
if __name__=="__main__":
    list=SingleCircularLinkedList()
    while True:
        option=int(input('Enter a Option:'))
        if option==1:
            value=int(input("Enter a Value:"))
            list.insertAtBegin(value)
        elif option==2:
            list.deleteAtBegin()
        elif option==3:
            data=int(input("Enter a Value:"))
            pos=int(input("Enter a Position:"))
            list.insertAtSpecificPosition(pos,data)
        elif option==4:
            pos=int(input("Enter a Position:"))
            list.deleteAtSpecificPosition(pos)
        elif option==5:
            value=int(input("Enter a Value:"))
            list.insertAtEnd(value)
        elif option==6:
            list.deleteAtEnd()
        elif option==7:
            list.display()
        elif option==8:
            exit(0)
        else:
            print('Enter a valid a Options')