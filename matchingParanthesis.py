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

        #bracket stacks
        self._paranthesis_open = Stack()
        self._paranthesis_close = Stack()
        self._square_open = Stack()
        self._square_close = Stack()
        self._curly_open = Stack()
        self._curly_close = Stack()
        #stack to keep track of index to be eliminated
        self._flagIndex = Stack()
        self._open = ['{','(','[']
        self._close = ['}',')',']']


    #function to remove all the flaged index from the list
    def cleanList(self,list):
        while not self._flagIndex.isEmpty():
            list.pop(self._flagIndex.peek())
            self._flagIndex.pop()
    

    #function to indentify umatched brackets and eliminates the bracket form input
    def checkBracket(self):
        cinput = list(self.input)
        _Limit = len(cinput)
        #checks in forward direction in terms of open brackets
        for i in range(_Limit):
            if cinput[i] in self._open:
                if cinput[i] == '(':
                    self._paranthesis_open.push(cinput[i])

                elif cinput[i] == '{':
                    self._curly_open.push(cinput[i])

                elif cinput[i] == '[':
                    self._square_open.push(cinput[i])

                
            elif cinput[i] in self._close:
                if cinput[i] == ')':
                    if self._paranthesis_open.isEmpty():
                        self._flagIndex.push(i)
                    else:
                        self._paranthesis_open.pop()

                elif cinput[i] == '}':
                    if self._curly_open.isEmpty():
                        self._flagIndex.push(i)
                    else:
                        self._curly_open.pop()

                elif cinput[i] == ']':
                    if self._square_open.isEmpty():
                        self._flagIndex.push(i)
                    else:
                        self._square_open.pop()

        self.cleanList(cinput)
        _Limit = len(cinput)
        #checks in backward direction in terms of closed brackets
        for j in range(_Limit -1, -1, -1):
            if cinput[j] in self._close:
                if cinput[j] == ')':
                    self._paranthesis_close.push(cinput[j])

                elif cinput[j] == '}':
                    self._curly_close.push(cinput[j])

                elif cinput[j] == ']':
                    self._square_close.push(cinput[j])

            if cinput[j] in self._open:
                if cinput[j] == '(':
                    if self._paranthesis_close.isEmpty():
                        self._flagIndex.push(j)
                    else:
                        self._paranthesis_close.pop()

                if cinput[j] == '{':
                    if self._curly_close.isEmpty():
                        self._flagIndex.push(j)
                    else:
                        self._curly_close.pop()

                if cinput[j] == '[':
                    if self._square_close.isEmpty():
                        self._flagIndex.push(j)
                    else:
                        self._square_close.pop()
        self.cleanList(cinput)

        self.output = self.output.join(cinput)       
        
#identify the unmatched paranthesis, remove it from string
input = "[(a+b){a-b][(a*b))]]"


def main():
    P = Parser(input)
    P.checkBracket()
    print("  Input : ",P.input)
    print("M_Input : ",P.output)
if __name__ == "__main__":
    main()
    
