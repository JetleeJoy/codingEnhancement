class Stack:
    def __init__(self,offset = -1):
        self.tos = offset
        self.stack = []
    
    #checking whether the stack is empty stack or not
    def isEmpty(self):
        if self.stack == []:
            return True
        else:
            return False

    #inserting an element into stack 
    def push(self,item):
        if self.tos == 536870912:
            print("Stack overflow  ! ")
        else:
            self.tos += 1
            self.stack.insert(self.tos,item )
            
    
    #deleting item from stack 
    def pop(self):
        if self.isEmpty():
            print("Stack underflow ! ")
        else:
            item = self.stack.pop(self.tos)
            print(item ," is deleted from stack")
            self.tos -= 1

    def peek(self):
        if self.stack == []:
            print("Empty Stack, ",end="")
            return self.tos
        else:
            return self.stack[self.tos]
    
    def iterate(self):
        for i in self.stack:
            if i == self.stack[self.tos]:
                print(i," -- > Stack Top")
            else:
                print(i)

def main():
    pass

if __name__ == "__main__":
    main()
    
