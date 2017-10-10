class Node:
    def __init__(self, val, prev_node=None, next_node=None):
        self.val = val
        self.prev_node = prev_node
        self.next_node = next_node
    
    def __repr__(self):
        return 'Node({0})'.format(self.val)

class LinkedList:

    def __init__(self):
        self.start_node = None
        self.current_node = None
        
    
    def add(self, val):
        n = Node(val)
        if not self.start_node:
            self.start_node = n
            
        else:
            self.current_node.next_node = n
            n.prev_node = self.current_node
        self.current_node = n
    @property
    def start(self):
        if not self.start_node:
            raise ValueError('No start node')
        return self.start_node
    
    @property
    def end(self):
        if not self.current_node:
            raise ValueError('No end node')
        return self.current_node
    
        
    def __iter__(self):
        _current_node = self.start_node
        while (_current_node):
            yield _current_node
            _current_node = _current_node.next_node
    
    def pop(self):
        #pop the last_node from thr right
        #O(1) time
        if not self.current_node:
            raise ValueError('No node to pop')
        if not self.current_node.prev_node:
            #this is the first node
            self.current_node = None
            self.start_node = None
        else:
            second_last_node = self.current_node.prev_node
            second_last_node.next_node = None
            self.current_node = second_last_node
    
    def popleft(self):
        #pop the left side of the node
        #O(1)time
        if not self.current_node:
            raise ValueError("No node to pop")

        if self.current_node is self.start_node:
            #this is the first node
            self.current_node = None
            self.start_node = None
        else:
            #remove the start node
            self.start_node = self.start_node.next_node


    @classmethod
    def from_list(cls, alist):
        self = cls()
        for item in alist:
            self.add(item)
        return self
    #this is awesome
    #there is nothing that
