
#TASK#01
# Implementing a Singly Linked List
# Objective: Understand and implement the basic operations of a Singly Linked List (SLL)





class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class SinglyLinkedList:

    def __init__(self):
        self.head = None
    
    def insert_at_beginning(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node
    
    def insert_at_end(self, data):
        new_node = Node(data)
        
        if self.head is None:
            self.head = new_node
            return
        
        current = self.head
        while current.next is not None:
            current = current.next
        current.next = new_node
    
    def insert_at_position(self, data, position):
        if position < 0:
            raise ValueError("Position must be non-negative")
            
        new_node = Node(data)
        
        if position == 0:
            self.insert_at_beginning(data)
            return
        
        current = self.head
        for _ in range(position - 1):
            if current is None:
                raise IndexError("Position out of range")
            current = current.next
        
        if current is None:
            raise IndexError("Position out of range")
            
        new_node.next = current.next
        current.next = new_node
    
    def delete_by_value(self, value):
        if self.head is None:
            raise ValueError("List is empty")
            
        if self.head.data == value:
            self.head = self.head.next
            return
        
        current = self.head
        while current.next is not None:
            if current.next.data == value:
                current.next = current.next.next
                return
            current = current.next
        
        raise ValueError("Value not found in list")
    
    def search(self, value):
        current = self.head
        position = 0
        
        while current is not None:
            if current.data == value:
                return position
            current = current.next
            position += 1
        
        return -1
    
    def display(self):
        """Display the linked list as a string"""
        elements = []
        current = self.head
        while current is not None:
            elements.append(str(current.data))
            current = current.next
        return " → ".join(elements) if elements else "Empty List"
    
    def __str__(self):
        return self.display()



def test_singly_linked_list():
    print("Testing Singly Linked List Operations")
    print("=" * 50)
    
    
    sll = SinglyLinkedList()
    print(f"Initial list: {sll}")
    

    sll.insert_at_beginning(3)
    sll.insert_at_beginning(2)
    sll.insert_at_beginning(1)
    print(f"After inserting 3, 2, 1 at beginning: {sll}")
    
    
    sll.insert_at_end(4)
    sll.insert_at_end(5)
    print(f"After inserting 4, 5 at end: {sll}")
    
    
    sll.insert_at_position(10, 2)
    print(f"After inserting 10 at position 2: {sll}")
    
    
    print("\nSearch operations:")
    print(f"Search for 3: Found at position {sll.search(3)}")
    print(f"Search for 5: Found at position {sll.search(5)}")
    print(f"Search for 99: {sll.search(99)} (not found)")
    
    
    print("\nDelete operations:")
    sll.delete_by_value(10)
    print(f"After deleting 10: {sll}")
    sll.delete_by_value(1)
    print(f"After deleting 1 (first node): {sll}")
    sll.delete_by_value(5)
    print(f"After deleting 5 (last node): {sll}")
    
    
    print("\nEdge cases:")
    empty_list = SinglyLinkedList()
    try:
        empty_list.delete_by_value(1)
    except ValueError as e:
        print(f"Attempt to delete from empty list: {e}")
    
    try:
        sll.insert_at_position(100, 10)
    except IndexError as e:
        print(f"Attempt to insert at invalid position: {e}")
    
    try:
        sll.delete_by_value(99)
    except ValueError as e:
        print(f"Attempt to delete non-existent value: {e}")
    
    print("\nFinal list state:")
    print(sll)


if __name__ == "__main__":
    test_singly_linked_list()


#Task #02

#  Detecting and Removing a Loop in a Linked List
# Objective: Learn how to detect and fix cycles in a linked list using Floyd’s Cycle Detection
# Algorithm. 

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None
    
    def append(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            return
        
        current = self.head
        while current.next:
            current = current.next
        current.next = new_node
    
    def create_loop(self, position):
        if position < 0:
            return
        last_node = self.head
        while last_node.next:
            last_node = last_node.next
        
        pos_node = self.head
        for _ in range(position):
            if not pos_node:
                return  
            pos_node = pos_node.next
        
        if pos_node:
            last_node.next = pos_node
    
    def detect_and_remove_loop(self):
        slow = fast = self.head
        loop_exists = False
        
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            if slow == fast:
                loop_exists = True
                break
        
        if not loop_exists:
            return None  
        slow = self.head
        while slow != fast:
            slow = slow.next
            fast = fast.next
        loop_start_node = slow
        ptr = loop_start_node
        while ptr.next != loop_start_node:
            ptr = ptr.next
        
        ptr.next = None  
        
        return loop_start_node.data
    
    def display(self, limit=20):
        """Display the linked list (with cycle protection)"""
        nodes = []
        current = self.head
        count = 0
        
        while current and count < limit:
            nodes.append(str(current.data))
            current = current.next
            count += 1
        
        if count == limit:
            nodes.append("... (possible loop)")
        
        return " → ".join(nodes) if nodes else "Empty List"



def test_loop_detection():
    print("Testing Loop Detection and Removal")
    print("=" * 50)
    
    
    ll = LinkedList()
    for i in range(1, 6):
        ll.append(i)
    
    print(f"Original list: {ll.display()}")
    
    ll.create_loop(2)
    print(f"\nAfter creating loop (5 → 3): {ll.display()}")
    
    
    loop_start = ll.detect_and_remove_loop()
    if loop_start:
        print(f"\nLoop detected at node with value: {loop_start}")
        print(f"After removing loop: {ll.display()}")
    else:
        print("No loop detected")
    

    ll2 = LinkedList()
    for i in range(1, 6):
        ll2.append(i)
    
    print("\nTesting list with no loop:")
    print(f"List: {ll2.display()}")
    loop_start = ll2.detect_and_remove_loop()
    print(f"Loop detection result: {loop_start}")


if __name__ == "__main__":
    test_loop_detection()

#Task#03
# Implementing a Doubly Linked List and Reverse Traversal
# Objective: Learn to work with Doubly Linked Lists (DLL) and perform reverse traversal.


class Node:
    def __init__(self, data):
        self.data = data
        self.prev = None
        self.next = None

class DoublyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
    
    def insert_at_beginning(self, data):
        new_node = Node(data)
        
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            new_node.next = self.head
            self.head.prev = new_node
            self.head = new_node
    
    def insert_at_end(self, data):
    
        new_node = Node(data)
        
        if self.tail is None:
            self.head = new_node
            self.tail = new_node
        else:
            new_node.prev = self.tail
            self.tail.next = new_node
            self.tail = new_node
    
    def delete_at_position(self, position):
        if self.head is None:
            raise IndexError("List is empty")
        
        if position < 0:
            raise ValueError("Position must be non-negative")
        
        current = self.head
        for _ in range(position):
            if current is None:
                raise IndexError("Position out of range")
            current = current.next
        
        if current is None:
            raise IndexError("Position out of range")
        
        if current.prev:
            current.prev.next = current.next
        else:  
            self.head = current.next
        
        if current.next:
            current.next.prev = current.prev
        else:  
            self.tail = current.prev
    
    def traverse_forward(self):
        elements = []
        current = self.head
        while current is not None:
            elements.append(str(current.data))
            current = current.next
        return " → ".join(elements) if elements else "Empty List"
    
    def traverse_backward(self):
        elements = []
        current = self.tail
        while current is not None:
            elements.append(str(current.data))
            current = current.prev
        return " → ".join(elements) if elements else "Empty List"
    
    def __str__(self):
        return self.traverse_forward()



def test_doubly_linked_list():
    print("Testing Doubly Linked List Operations")
    print("=" * 50)
    
    
    dll = DoublyLinkedList()
    print(f"Initial list (forward): {dll}")
    print(f"Initial list (reverse): {dll.traverse_backward()}")
    
    
    dll.insert_at_beginning(3)
    dll.insert_at_beginning(2)
    dll.insert_at_beginning(1)
    print(f"\nAfter inserting 3, 2, 1 at beginning:")
    print(f"Forward: {dll}")
    print(f"Reverse: {dll.traverse_backward()}")
    

    dll.insert_at_end(4)
    dll.insert_at_end(5)
    print(f"\nAfter inserting 4, 5 at end:")
    print(f"Forward: {dll}")
    print(f"Reverse: {dll.traverse_backward()}")
    

    print("\nDelete operations:")
    dll.delete_at_position(2)  
    print(f"After deleting position 2:")
    print(f"Forward: {dll}")
    print(f"Reverse: {dll.traverse_backward()}")
    
    dll.delete_at_position(0)  
    print(f"\nAfter deleting position 0 (first node):")
    print(f"Forward: {dll}")
    print(f"Reverse: {dll.traverse_backward()}")
    
    dll.delete_at_position(2) 
    print(f"\nAfter deleting position 2 (last node):")
    print(f"Forward: {dll}")
    print(f"Reverse: {dll.traverse_backward()}")
    
    
    print("\nEdge cases:")
    empty_list = DoublyLinkedList()
    try:
        empty_list.delete_at_position(0)
    except IndexError as e:
        print(f"Attempt to delete from empty list: {e}")
    
    try:
        dll.delete_at_position(5)
    except IndexError as e:
        print(f"Attempt to delete at invalid position: {e}")


if __name__ == "__main__":
    test_doubly_linked_list()