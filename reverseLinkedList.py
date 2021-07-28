
#implementing linked list

class Node:
    #initilizing a new node type
    def __init__(self, d, r = None):
        self.data = d # data for individual nodes 
        self.next_node = r # next node link
    
    #to retrive next node 
    def get_next(self):
        return self.next_node
    #to set next node
    def set_next(self, r):
        self.next_node = r
    #to retrive data of node
    def get_data(self):
        return self.data
    #to set data to node
    def set_data(self, d):
        self.data = d


class linkedList():
    #initlizing a new list object
    def __init__(self,r = None):
        self.root = r #root node, points to first node in list
        self.size = 0 #keeps track of the size of the list
    #to get the size of list
    def get_size(self):
        return self.size
    
    #adding a new element infront of list
    def prepend(self, d):
        new_node = Node(d,self.root)
        self.root = new_node
        self.size += 1
    #removing the last element of list
    def pop(self):
        this_node = self.root
        prev_node = None
        while True:
            if this_node.get_next() == None:
                if prev_node is not None:
                    prev_node.set_next(None)
                    self.size -= 1
                else:
                    print("Empty list")
                    self.__init__()
                break
            prev_node = this_node
            this_node = this_node.get_next()
    #removing an element of specific data
    def remove(self, d):
        this_node = self.root
        prev_node = None 
        while this_node is not None:
            if this_node.get_data() == d:
                if prev_node is not None:
                    prev_node.set_next(this_node.get_next())
                else:
                    self.root = this_node.get_next()
                self.size -= 1
            prev_node = this_node
            this_node = this_node.get_next()
    #checking the existence of a specific data inside the list
    def find(self, d):
        this_node = self.root
        while this_node is not None:
            if this_node.get_data() == d:
                return True
            elif this_node.get_next() == None:
                return False
            else:
                this_node = this_node.get_next()
    #iterating the entire list 
    def iterate(self):
        this_node = self.root
        while True:
            if this_node == None:
                print("Empty list")
                break
            else:
                print(this_node.get_data()," -> ",end='')
                if this_node.get_next() == None:
                    print("None")
                    break
                else:
                    this_node = this_node.get_next()
    #insert element at a specific postition
    def insert(self, pos, d):
        new_node = Node(d)
        this_node = self.root
        prev_node = None
        track = 1
        if pos == 1:
            self.prepend(d)
        else:
            while this_node is not None:
                prev_node = this_node
                this_node = this_node.get_next()
                track += 1
                if pos <= 0:
                    print("Invalid index ! ")
                    break
                elif pos > self.get_size():
                    print("out of bound index error")
                    break
                elif pos == track:
                    new_node.set_next(prev_node.get_next())
                    prev_node.set_next(new_node)
                    self.size += 1
                    break

    #reverse the list 
    def reverse(self):
        if self.get_size() == 0:
            print("empty list")
            return False
        elif self.get_size() == 1:
            return True
        else:
            #croot = self.root
            temp = self.root
            self.root = temp.get_next()
            temp.set_next(None)
            while self.root is not None:
                if self.root.get_next() == None:
                    self.root.set_next(temp)
                    return True
                else:
                    temp2 = self.root
                    self.root = temp2.get_next()
                    temp2.set_next(temp)
                    temp = temp2

# external function 
def reverseList(llist):
    if llist.get_size() == 0:
        print("Empty list")
    elif llist.get_size() == 1:
        return True
    else:
        temp = llist.root
        llist.root = temp.get_next()
        temp.set_next(None)
        while llist.root is not None:
            if llist.root.get_next() == None:
                llist.root.set_next(temp)
                return True
            else:
                temp2 = llist.root
                llist.root = temp2.get_next()
                temp2.set_next(temp)
                temp = temp2


def main():
    llist = linkedList()
    llist.insert(1,5)
    llist.insert(1,4)
    llist.insert(1,6)
    llist.insert(1,34)
    llist.insert(1,32)
    llist.insert(1,522)
    llist.insert(1,34)
    llist.iterate()
    if reverseList(llist):
        llist.iterate()

if __name__ == "__main__":
    main()
        

    
