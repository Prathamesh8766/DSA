class Node:
    def __init__(self,data,next=None,pre=None):
        self.data = data
        self.next = next
        self.pre = pre

class DoubleLinklist:
    def __init__(self):
        self.head = None
        self.tail = None
    
    def creationOfDoubleLinklist(self):

        size = int(input("Enter Size:"))

        self.head = Node(input("Enter data for the head:"))
        self.tail = self.head
        current = self.head
        for i in range(1,size):

            data = input("Enter Data :")

            new_node = Node(data,pre=current)
            current.next= new_node
            current = new_node
            self.tail = current
        return self.head

    def display(self,reverse=False):
        if self.head is None:
            print("Double link list is empty")
            return
        if reverse ==False:
            current = self.head
            print("None <-> ", end="")
            while current:
                print(current.data, end=" <-> ")
                current = current.next
        else:
            current = self.tail
            print("None <-> ", end="")
            while current:
                print(current.data, end = " <-> ")
                current = current.pre
        print("None")

    def insetAthead(self):
        new_node = Node(input("Enter data:"),next=self.head)
        self.head.pre = new_node
        self.head = new_node
    
    def append(self):
        new_node = Node(input("Enter data: "))
        
        if self.head is None:
            self.head = new_node
            self.tail = new_node
            return
        
        new_node.pre = self.tail
        self.tail.next = new_node
        self.tail = new_node
        return

    def deleteHead(self):
        if self.head == None:
            print("List is empty")
        self.head = self.head.next
        self.head.pre = None
    def middleNode(self):
        current = self.head
        l =0
        a = []
        pre_mid = None
        while current:
            l += 1
            mid = -(-l//2) 
            a.append(current.data)
            if mid == pre_mid :
                a.pop(0)
            pre_mid = mid
            current = current.next
        return a


    
    
            

l1 = DoubleLinklist()
l1.creationOfDoubleLinklist()
print(l1.middleNode())
l1.display()
# l1.append()
# l1.display(True)
# l1.deleteHead()
# l1.display()
