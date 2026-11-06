class Node:
    def __init__(self, data, next=None):
        self.data = data
        self.next = next

class SinglyLL:
    def __init__(self):
        self.head = None
    
    ''' Traversal '''
    def print_list(self):
        cur = self.head
        while cur:
            print(cur.data, end=' -> ')
            cur = cur.next
        print('None')
    
    ''' Insertion '''
    def insert_at_beginning(self, data):
        new_node = Node(data, self.head)
        self.head = new_node
    
    def insert_at_end(self, data):
        if self.head is None:
            self.head = Node(data)
            return
        
        cur = self.head
        while cur.next:
            cur = cur.next
        cur.next = Node(data)
    
    def insert_at_index(self, data, index):
        if index < 0:
            raise Exception('Invalid index')
        
        if index == 0:
            self.insert_at_beginning(data)
            return
        
        count = 0
        cur = self.head
        while cur:
            if count == index - 1:
                new_node = Node(data, cur.next)
                cur.next = new_node
                break
            cur = cur.next
            count += 1
        
        if cur is None:
            raise Exception('Invalid index')
        

    ''' Deletion '''
    def delete_at_beginning(self):
        if not self.head:
            return
        
        self.head = self.head.next

    def delete_at_end(self):
        if not self.head:
            return
        
        if not self.head.next:
            head = None
            return
        
        second_last = self.head
        while second_last.next.next:
            second_last = second_last.next
        
        second_last.next = None

    def delete_at_index(self, index):
        if not self.head or index < 0:
            raise Exception('Invalid index')
            
        if index == 0:
            self.delete_at_beginning()
            return
    
        current = self.head
        while current.next.next and index > 1:
            current = current.next
            index -= 1

        if index > 1:    
            raise Exception('Invalid index')

        current.next = current.next.next    
    
    ''' Search '''
    # Iterative search function
    def search(self, key):
        cur = self.head
        while cur:
            if cur.data == key:
                return True
            cur = cur.next
        return False

    # Recursive search function
    def search_recursive(self, node, key):
        # Base case
        if not node:
            return False
        
        if node.data == key:
            return True
        
        return self.search_recursive(node.next, key)

    ''' Replacement '''
    def update_data(self, old_data, new_data):
        cur = self.head
        while cur:
            if cur.data == old_data:
                cur.data = new_data
                return
            cur = cur.next
        raise Exception('Data not found')
    
    def update_idx(self, index, new_data):
        if index < 0:
            raise Exception('Invalid index')
        
        cur = self.head
        count = 0
        while cur:
            if count == index:
                cur.data = new_data
                return
            cur = cur.next
            count += 1

        raise Exception('Invalid index')
    
