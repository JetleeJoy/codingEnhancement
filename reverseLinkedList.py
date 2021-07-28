
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

def main():
    pass

if __name__ == "__main__":
    main()
        

    