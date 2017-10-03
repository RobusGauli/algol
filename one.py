#here is the first algorithm in the list

#a standart way to create a node

class Node:
    
    def __init__(self, val, next_node=None):
        self.val = val
        self.next_node = next_node

    def __repr__(self):
        return 'Node({0})'.format(self.val)


class LinkedList:

    def __init__(self):
        self.start_node = None
        self.current_node = None
    
    def add(self, value):
        #create a node out of the value
        n = Node(value)
        #if there is no start node then it is the start node 
        if not self.start_node:
            self.start_node = n
            
        else:
            #this is the next_node of the current_node
            self.current_node.next_node = n
        self.current_node = n
    
    # a method to iterate 

    def __iter__(self):
        _current_node = self.start_node
        while (_current_node):
            yield _current_node
            _current_node = _current_node.next_node
        


