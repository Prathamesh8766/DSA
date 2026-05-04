class Node:
   def  __init__(self,data,next=None):
        self.data = data
        self.next = next

class LinkList:

    def __init__(self):
        self.head = None

    def createLinkList(self):   
        size = int(input("Enter the size of linList:"))
        if size <=0:
            return None
        self.head = Node(int(input("Enter the data for head node:")))
        current = self.head

        for i in range(1,size):
            data = int(input("Enter data:"))
            new_node = Node(data)
            current.next = new_node
            current = new_node
        

    def displayLinkList(self): # Display list
        current = self.head
        while current:
            print(current.data, end="->")
            current = current.next
        print("None")

    def insetAtHead(self): # Insert At Head
        new_node = Node(int(input("Enter New head Data:")), self.head)
        self.head = new_node
        return self.head

    def deleteNode(self,val): # delete NOde

        if self.head is None:
            print("List is empty")
            return

        if self.head.data == val:
            self.head = self.head.next
            print(f"Delete {val} from the list")
            return
        current = self.head

        while current.next:
            if current.next.data == val:
                
                current.next = current.next.next
                return
            current = current.next
    
    def findLength(self): # find linklist 
        if self.head is None:
            print("Lenght of LinkList is 0")
            return 
        current = self.head
        length = 0
        while current:
            length += 1
            current = current.next
        print("Length of linlist is ", length)
    
    def searchInLinklist(self,val):
        if self.head is None:
            print("Link list is empty")
            return
        current = self.head
        while current:
            if current.data == val:
                print("True")
                return True
            current =current.next
        print("False")
        return False




l1 = LinkList()
l1.createLinkList()
l1.displayLinkList()
l1.findLength()
l1.searchInLinklist("5")
l1.searchInLinklist(3)
