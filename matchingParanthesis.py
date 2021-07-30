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
        self.open = {
             '{': 1,
             '[': 2,
             '(': 3
            }   

        self.close = {
             '}': -1,
             ']': -2,
             ')': -3
            }

        self.input = inputString
        self.output = ""
        self._paranthesis = Stack()

    #analyzing the brackets
    def checkBracket(self):
        cinput = self.input #generate a copy of string
        cinput = list(cinput) #created a list out of string
        for char in cinput:
            if char in self.open.keys():
                for btype in self.open.keys():
                    if char == '(': 
                        self._paranthesis.push(self.open[btype])
            elif char in self.close.keys():
                for btype in self.close.keys():
                    if char == ')':
                        if self._paranthesis.isEmpty():
                            cinput.remove(char)
                        else:
                            self._paranthesis.pop()     
        self.output = self.output.join(cinput)


#identify the unmatched paranthesis, remove it from string
input = "((a+b)+c))"


def main():
    P = Parser(input)
    P.checkBracket()
    print(P.output)
if __name__ == "__main__":
    main()
    
