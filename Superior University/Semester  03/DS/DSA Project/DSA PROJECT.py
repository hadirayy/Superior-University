from collections import deque
class Book:
    def __init__(self, book_id, title, author, copies=1):
        self.book_id = book_id
        self.title = title
        self.author = author
        self.copies = copies

    def __repr__(self):
        return f"{self.book_id}: {self.title} by {self.author} | Available: {self.copies}"

class BSTNode:
    def __init__(self, book):
        self.book = book
        self.left = None
        self.right = None

class BookBST:
    def __init__(self):
        self.root = None

    def insert(self, book):
        def _insert(node, book):
            if not node:
                return BSTNode(book)
            if book.book_id < node.book.book_id:
                node.left = _insert(node.left, book)
            else:
                node.right = _insert(node.right, book)
            return node
        self.root = _insert(self.root, book)

    def search(self, book_id):
        def _search(node, book_id):
            if not node:
                return None
            if book_id == node.book.book_id:
                return node.book
            elif book_id < node.book.book_id:
                return _search(node.left, book_id)
            else:
                return _search(node.right, book_id)
        return _search(self.root, book_id)

    def inorder(self, node=None):
        if node is None:
            node = self.root
        result = []
        if node.left:
            result += self.inorder(node.left)
        result.append(node.book)
        if node.right:
            result += self.inorder(node.right)
        return result
class IssuedBookNode:
    def __init__(self, book):
        self.book = book
        self.next = None

class IssuedBooksLinkedList:
    def __init__(self):
        self.head = None

    def issue(self, book):
        new_node = IssuedBookNode(book)
        new_node.next = self.head
        self.head = new_node

    def return_book(self, book_id):
        prev = None
        curr = self.head
        while curr:
            if curr.book.book_id == book_id:
                if prev:
                    prev.next = curr.next
                else:
                    self.head = curr.next
                return curr.book
            prev = curr
            curr = curr.next
        return None

    def list_books(self):
        result = []
        curr = self.head
        while curr:
            result.append(curr.book)
            curr = curr.next
        return result

class ReturnStack:
    def __init__(self):
        self.stack = []

    def push(self, book):
        self.stack.append(book)

    def pop(self):
        return self.stack.pop() if self.stack else None

class IssueQueue:
    def __init__(self):
        self.queue = deque()

    def enqueue(self, user_id, book_id):
        self.queue.append((user_id, book_id))

    def dequeue(self):
        return self.queue.popleft() if self.queue else None

class User:
    def __init__(self, user_id, name):
        self.user_id = user_id
        self.name = name
        self.issued_books = IssuedBooksLinkedList()

    def issue_book(self, book):
        self.issued_books.issue(book)

    def return_book(self, book_id):
        return self.issued_books.return_book(book_id)

    def list_books(self):
        return self.issued_books.list_books()

book_bst = BookBST()
return_stack = ReturnStack()
issue_queue = IssueQueue()
users = {}

book_bst.insert(Book(1, "Python Basics", "Hamza", 3))
book_bst.insert(Book(102, "Data Structures", "Ahmed", 2))
book_bst.insert(Book(3, "Algorithms", "Umer", 3))
book_bst.insert(Book(103, "Data Science", "Haider",4 ))
book_bst.insert(Book(4, "Html Css", "Hadi",4 ))
def add_user():
    user_id = input("Enter User ID: ")
    name = input("Enter Name: ")
    if user_id in users:
        print("User ID already exists!")
        return
    users[user_id] = User(user_id, name)
    print("User added.")


def issue_book():
    user_id = input("User ID: ")
    if user_id not in users:
        print("User not found.")
        return
    book_id = int(input("Book ID to issue: "))
    user = users[user_id]
    book = book_bst.search(book_id)
    if book and book.copies > 0:
        book.copies -= 1
        user.issue_book(book)
        print(f"Issued '{book.title}' to {user.name}")
    else:
        print("Book unavailable, added to waitlist.")
        issue_queue.enqueue(user_id, book_id)

def return_book():
    user_id = input("User ID: ")
    if user_id not in users:
        print("User not found.")
        return
    book_id = int(input("Book ID to return: "))
    user = users[user_id]
    book = user.return_book(book_id)
    if book:
        book.copies += 1
        return_stack.push(book)
        print(f"{book.title} returned.")
    else:
        print("Book not issued to this user.")
def view_user_books():
    user_id = input("User ID: ")
    if user_id not in users:
        print("User not found.")
        return
    books = users[user_id].list_books()
    print(f"Issued Books for {users[user_id].name}:")
    for b in books:
        print(f" - {b}")
while True:
    print("\n=== Library Management Menu ===")
    print("1. Add User")
    print("2. Issue Book")
    print("3. Return Book")
    print("4. View Issued Books")
    print("5. List All Books")
    print("6. Exit")
    choice = input("Choose: ")

    if choice == "1":
        add_user()
    elif choice == "2":
        issue_book()
    elif choice == "3":
        return_book()
    elif choice == "4":
        view_user_books()
    elif choice == "5":
        for book in book_bst.inorder():
            print(book)
    elif choice == "6":
        print("Exiting system...")
        break
    else:
        print("Invalid choice.")

