#punto1.5
class Node():
    def __init__ (self, prev=None, data=None,next=None):
        self.data = data
        self.next = next
        self.prev = prev

class DLL():
    def __init__ (self):
        self.head=None
        self.tail=None
        self.size=0
        
    def append (self,data):
        new_node = Node(None,data,None)
        
        if self.head is None:
            self.head = new_node
            self.tail = self.head
        else:
            new_node.prev = self.tail
            self.tail.next =new_node
            self.tail = new_node
        self.size += 1
        
    def get(self,index):
        
        if(index <= (self.size//2)):
            
            current_node = self.head
            
            for i in range(index-1):
                current_node = current_node.next
                
        if(index>(self.size/2)):
            
            current_node=self.tail
            
            for i in range(index-1):
                current_node=current_node.prev
                
        return current_node
        
    def insert_before(self,data,index):
        
        new_node = Node(None,data,None)
        if self.head is None:
            self.head = new_node
            self.tail = self.head
            self.size +=1
        elif index == self.size:
            self.append(data)
        elif index < self.size:
            inserting_before = self.get(index)
            
            new_node.prev = inserting_before.prev
            inserting_before.prev = new_node
            new_node.next = inserting_before
            
            if(new_node.prev != None):
                new_node.prev.next = new_node
                
            if index ==0:
                self.head  = new_node
            self.size += 1
        else:
            print("Index not reachable")
            
        def delete(self, index):
            
            to_delete =self.get(index)
            
            if to_delete.prev != None:
                to_delete.prev.next = to_delete.next
            elif to_delete.prev is None:
                self.head = to_delete.next
            elif to_delete.next is None:
                self.tail = to_delete.prev
            self.size -= 1
        
    
      
