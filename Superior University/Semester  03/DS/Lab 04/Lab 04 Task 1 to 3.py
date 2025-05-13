#Task #01
# Implementing a Stack Using Arrays and Linked Lists
# Understand stack operations and implement a stack using two different data stucture





class ArrayStack:
    def __init__(self):
        self.items = []
    def push(self, item):
        self.items.append(item)
    def pop(self):
        if self.is_empty():
            raise IndexError("Pop from empty stack")
        return self.items.pop()
    def peek(self):
        if self.is_empty():
            raise IndexError("Peek from empty stack")
        return self.items[-1]
    def is_empty(self):
        return len(self.items) == 0
    def size(self):
        return len(self.items)
    def __str__(self):
        return f"Stack({self.items})"
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
class LinkedListStack:
    def __init__(self):
        self.top = None
        self._size = 0
    def push(self, item):
        new_node = Node(item)
        new_node.next = self.top
        self.top = new_node
        self._size += 1
    def pop(self):
        if self.is_empty():
            raise IndexError("Pop from empty stack")
        item = self.top.data
        self.top = self.top.next
        self._size -= 1
        return item
    def peek(self):
        if self.is_empty():
            raise IndexError("Peek from empty stack")
        return self.top.data
    def is_empty(self):
        return self.top is None
    def size(self):
        return self._size
    def __str__(self):
        items = []
        current = self.top
        while current:
            items.append(str(current.data))
            current = current.next
        return f"Stack({' -> '.join(reversed(items))})" if items else "Stack()"
def test_stack(stack_class, name):
    print(f"\nTesting {name} Implementation")
    print("=" * 40)
    stack = stack_class()
    print(f"Initial stack: {stack}")
    print(f"Is empty? {stack.is_empty()}")
    print("\nPushing items:")
    for i in range(1, 6):
        stack.push(i)
        print(f"After push({i}): {stack}")
    print(f"\nCurrent stack: {stack}")
    print(f"Peek: {stack.peek()}")
    print(f"Size: {stack.size()}")
    print("\nPopping items:")
    while not stack.is_empty():
        print(f"Popped: {stack.pop()}, Remaining: {stack}")
    print("\nTesting empty stack behavior:")
    try:
        stack.pop()
    except IndexError as e:
        print(f"pop() on empty stack: {e}")
    try:
        stack.peek()
    except IndexError as e:
        print(f"peek() on empty stack: {e}")
test_stack(ArrayStack, "Array Stack")
test_stack(LinkedListStack, "Linked List Stack")


#Task#02
# Evaluating Postfix Expressions Using Stacks
# Objective: Apply the stack data structure to solve an arithmetic expression evaluation
# problem.

def evaluate_postfix(expression):
    stack = []
    tokens = expression.split()
    
    for token in tokens:
        if token.isdigit() or (token[0] == '-' and token[1:].isdigit()):
            stack.append(int(token))
        else:
            if len(stack) < 2:
                raise ValueError("Invalid postfix expression")
            right = stack.pop()
            left = stack.pop()
            if token == '+':
                result = left + right
            elif token == '-':
                result = left - right
            elif token == '*':
                result = left * right
            elif token == '/':
                if right == 0:
                    raise ZeroDivisionError("Division by zero")
                result = left / right
            else:
                raise ValueError(f"Unknown operator: {token}")
            stack.append(result)
    
    if len(stack) != 1:
        raise ValueError("Invalid postfix expression")
    return stack[0]
def test_postfix_evaluation():
    print("Testing Postfix Expression Evaluation")
    print("=" * 50)
    
    test_cases = [
        ("5 1 2 + 4 * + 3 -", 14),    
        ("3 4 +", 7),                  
        ("10 5 /", 2),                 
        ("2 3 * 4 +", 10),             
        ("4 2 5 * + 1 3 2 * + /", 2),  
        ("-5 3 +", -2),                
        ("1 2 3 4 5 * * * +", 121),   
    ]
    
    for expr, expected in test_cases:
        try:
            result = evaluate_postfix(expr)
            print(f"Expression: {expr}")
            print(f"Expected: {expected}, Got: {result}")
            print(f"{'✓ PASS' if result == expected else '✗ FAIL'}")
            print("-" * 40)
        except Exception as e:
            print(f"Error evaluating '{expr}': {e}")
            print("-" * 40)
    error_cases = [
        ("5 1 + +", "Invalid postfix expression"),         
        ("1 2 ?", "Unknown operator"),                    
        ("1 0 /", "Division by zero"),                
        ("1 2 3 +", "Invalid postfix expression"),      
    ]
    
    print("\nTesting Error Cases")
    print("=" * 40)
    for expr, expected_error in error_cases:
        try:
            result = evaluate_postfix(expr)
            print(f"Expression: {expr} unexpectedly succeeded with result: {result}")
        except Exception as e:
            print(f"Expression: {expr}")
            print(f"Expected error: {expected_error}, Got: {type(e).__name__}: {e}")
            print(f"{'✓ PASS' if expected_error in str(e) else '✗ FAIL'}")
            print("-" * 40)

if __name__ == "__main__":
    test_postfix_evaluation()

# Task 3: Implementing a Circular Queue 
# Objective: Implement a circular queue and compare it with a linear queue.

class CircularQueue:
    def __init__(self, size):
        self.size = size
        self.queue = [None] * size
        self.front = -1
        self.rear = -1
    def is_empty(self):
        return self.front == -1
    def is_full(self):
        return (self.rear + 1) % self.size == self.front
    def enqueue(self, element):
        if self.is_full():
            print("Queue is full! Cannot enqueue.")
            return
        if self.front == -1:
            self.front = 0
        self.rear = (self.rear + 1) % self.size
        self.queue[self.rear] = element

    def dequeue(self):
        if self.is_empty():
            print("Queue is empty! Cannot dequeue.")
            return None
        
        element = self.queue[self.front]
        if self.front == self.rear:
            self.front = -1
            self.rear = -1
        else:
            self.front = (self.front + 1) % self.size
        return element

    def front_element(self):
        if self.is_empty():
            print("Queue is empty! No front element.")
            return None
        return self.queue[self.front]
    def rear_element(self):
        if self.is_empty():
            print("Queue is empty! No rear element.")
            return None
        return self.queue[self.rear]
cq = CircularQueue(5)
cq.enqueue(10)
cq.enqueue(20)
cq.enqueue(30)
cq.enqueue(40)
cq.enqueue(50)
print(f"After enqueueing 5 elements: {cq.queue}")
cq.enqueue(60)  
print(f"Dequeued element: {cq.dequeue()}")
print(f"Queue after dequeue: {cq.queue}")
cq.enqueue(60)
print(f"Queue after enqueueing 60: {cq.queue}")
print(f"Front element: {cq.front_element()}")  
print(f"Rear element: {cq.rear_element()}")    

