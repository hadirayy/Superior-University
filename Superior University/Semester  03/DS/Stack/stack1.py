class Stack:
    def __init__(self,limit):
        self.stack=[]
        self.limit=limit
    def push(self):
        if len(self.stack) == self.limit:
            print("Stack is already full")
        else:
            for i in range(self.limit - len(self.stack)):
                element=int(input("Enter the number:"))
                self.stack.append(element)
                print("updating Stack is ",self.stack)
    def pop(self):
        if not self.stack:
            print("Stack is Already Empty, and no value in stack to remove")
        else:
            e = self.stack.pop()
            print("Removed value trom stack is:",e)
            print("Updating Stack is :",self.stack)

    def display(self):
        if not self.stack:
            print("Stack is empty")
        else:
            for i in self.stack:
                print(i)
    def sorting(self):
        if not self.stack:
            print("Stack is empty ,no value in the stack is to be arranged ")
        else:
            self.stack.sort()
            print("Sorting Stacck in Accending order:",self.stack)
            self.stack.sort(reverse= True)
            print("Sorting Stack in decending order:",self.stack,)
    def PeakValue(self):
        if len(self.stack) == 0:
            print("Stack is empty,and their is no peak and top value ")
        else:
            print("Peak value:",self.stack[-1])

limit=int(input("Enter the value:"))
obj=Stack(limit)
obj.push()
obj.display()
obj.sorting()
obj.PeakValue()
print(obj)
print("----stacking program----")
print("1, push vlaue")
print("2, Display   ")
print("3, Sor(ting Values")
print("4, Peal value")
print("5, Exit")
while True:

    choice=int(input("Enter the number"))
    if choice == 1:
        obj.push()
    elif choice == 2:
        obj.display()
    elif choice == 3:
        obj.PeakValue()
    elif choice == 4:
        obj.sorting()
    elif choice == 5:
        print("Exiting the program.")
        break
    else:
        print("Invalid choice, please try again.")


