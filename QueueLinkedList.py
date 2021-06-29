# Queue Implementation (two pointers are maintained i.e. Rear and Front)
# Operations are :
# 1. pop operation (to insert element at rear)
# 2. push operation (to delete element from front)
# 3. peek operation (displays topmost element)
# 4. showList (queue traversal)
class QueueLinkedList:
    front = None                    # deletion from front end
    rear = None                     # insertion from rear end

    class Node:
        data = None
        next = None

    def push(self, value):
        node = self.Node()
        node.data = value
        node.next = None
        if (self.front == None):
            self.front = node
            self.rear = node
        else:
            self.rear.next=node
            self.rear = node

    def pop(self):
        if (self.front == None):
            print("Queue is empty!")
        else:
            self.front=self.front.next

    def peek(self):
        if self.front == None:
            print("No element in queue")
        else:
            print(self.rear.data)

    def showList(self):
        if (self.front == None):
            print("List is empty")
        else:
            temp = self.front
            while (temp != None):
                print(temp.data, end=' ')
                temp = temp.next

    # This function helps in execution of the other functions (that perform various Linkedlist operations)
    def perform(self):
        print("1- PUSH")
        print("2- POP")
        print("3- PEEP")
        print("4- SHOW LIST")
        print("5- EXIT")
        continue_operation = 1
        while (continue_operation):
            ch = int(input("Enter the choice of operation : "))
            if ch == 1:
                val = int(input("Enter the element to insert : "))
                self.push(val)
            elif ch == 2:
                self.pop()
            elif ch == 3:
                self.peek()
            elif ch == 4:
                print("The list is : ", end="")
                self.showList()
                print()
            elif ch == 5:
                print("Quiting as per your wish !")
                exit()
            else:
                print("Wrong choice of operation")
            continue_operation=int(input("Do you want to continue ? (0--> No and 1-->Yes) : "))

# we are creating a linkedlist object
s = QueueLinkedList()
s.perform()