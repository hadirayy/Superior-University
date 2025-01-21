class Queue:
    def __init__(self):
        self.queue=[]
        self.limit  =int(input("Enteer the Limit value:"))
    def enqueue(self):
        if len(self.queue) == self.limit:
            print("Queue is already filled")
        else:
            for i in  range(self.limit -len(self.queue)):
                e =input("Enter Value for Queue:")
                self.queue.append(e)
                print("Updated Queue:",self.queue)


    def dequeue(self):
        if len(self.queue)==0:
            print("Queue is already")
        else:
            e = self.queue.pop(0)
            print("Removed value from the ueue is :",e)
            print("Updated Queue:",self.queue)
obj=Queue()
obj.enqueue()
obj.dequeue()
print(obj)
print("----Queue---")
print("1.Enueue")
print("2.Dequeue")
print("3.Exit")
while True:
    choice=int(input("Enter the number :"))
    if choice == 1:
        obj.enqueue()
    elif choice == 2:
        obj.dequeue()
    elif choice == 3:
        print("Exit the Program.")
        break
    else:
        print("Invalid Number ")

    






    
        

                    

                