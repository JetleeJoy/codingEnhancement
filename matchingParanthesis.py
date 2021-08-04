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
            #print(item ," is deleted from stack")
            self.tos -= 1
    #to display the element at top of stack
    def peek(self):
        if self.stack == []:
            print("Empty Stack, ",end="")
            return self.tos
        else:
            return self.stack[self.tos]
    # to view the full stack
    def iterate(self):
        for i in self.stack:
            print(i)

class Parser:
    def __init__(self,inputString):
        #create dictionary for parser
        self.input = inputString
        self.output = ""
        self._paranthesis_open = Stack()
        self._paranthesis_close = Stack()
        self._flagIndex = Stack()
    
    #function to remove all the flaged index from the list
    def cleanList(self,list):
        while not self._flagIndex.isEmpty():
            list.pop(self._flagIndex.peek())
            self._flagIndex.pop()

    #function to check for disparity in barckets
    def checkBracket(self):
        cinput = self.input #generate a copy of string
        cinput = list(cinput) #created a list out of string
        _Limit = len(cinput)
        
        for i in range(_Limit):
            if cinput[i] == '(':
                self._paranthesis_open.push(cinput[i])
            elif cinput[i] == ')':
                if self._paranthesis_open.isEmpty():
                    self._flagIndex.push(i)
                else:
                    self._paranthesis_open.pop()
        self.cleanList(cinput)
        _Limit = len(cinput)
        for j in range(_Limit -1, -1, -1):
            if cinput[j] == ')':
                self._paranthesis_close.push(cinput[j])
            elif cinput[j] == '(':
                if self._paranthesis_close.isEmpty():
                    self._flagIndex.push(j)
                else:
                    self._paranthesis_close.pop()
        self.cleanList(cinput)
        self.output = self.output.join(cinput)

#identify the unmatched paranthesis, remove it from string
input = "((((a+b(a-b)(a+b))(a*b)))"


def main():
    P = Parser(input)
    P.checkBracket()
    print("  Input : ",P.input)
    print("M_Input : ",P.output)
if __name__ == "__main__":
    main()
    
