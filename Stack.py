class arrayStack:
    array=[]

    def push(self,data):
        self.array.append(data)
        return
    
    def pop(self):
        self.array.pop()
        return
    
    def display(self):
        print(self.array)
        return
    

if __name__=="__main__":
    s=arrayStack()
    while(True):
        option=int(input('Enter a Option:'))
        if option == 1:
            data=int(input('Enter a Value:'))
            s.push(data)
        elif option == 2:
            s.pop()
        elif option==3:
            s.display()
        elif option==4:
            exit(0)
        else:
            print('Enter a valid option')