class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
        


# def Create_linklist():
#     size= int(input("Enter link list size : "))

#     if size<=0:
#         print("Not Allowed")
#         return None
    
#     data = input("Enter the data at node : ")
#     head=Node(data)
#     current=head

#     for i in range(2,size+1):

#         data=input(f"Enter the data {i} node : ")

#         node= Node(data)
#         current.next=node
#         current=node
#     return head

# # l1= Create_linklist()
# # print(l1)
# # print(l1.next.data)

# def Create_linklist_recurrsion(size):
#     if size<= 0:
#         return None
#     data=input(f"Enter the data at {size} : " )
#     node =Node(data)
#     node.next=Create_linklist_recurrsion(size-1)

#     return node

# l2=Create_linklist_recurrsion(3)
# print(l2)
# print(l2.next.data)
s="madac"
print(s[-1])
head= None
def create_link_list():
    i= int(input("Enter input :"))

    if i== -1:
        return
    
    node= Node(i)
    global head
    if head is None:
        head = node
    
    
    node.next = create_link_list()
    return node


create_link_list()

def link_list_display(temp):

    if temp==None:
        return
    print(temp.data)
    link_list_display(temp.next)
    
    
print("fist")
print()
link_list_display(head)

# def insert_at_front(target,head):
    
#     if head== None:
#         return 0
    
#     if head.data==target:
#         data= int(input("Enter data : "))
#         node=Node(data)
#         node.next =head.next
#         head.next= node

#     insert_at_front(target,head.next)    
# insert_at_front(5,head)     
# link_list_display(head)   


# def delete(target,head):
#     if head == None :
#         return None
#     if head.data== target:
#         return head.next
#     else:
#          head.next=delete(target,head.next)
#          return head
    

# print("deleted 5")
# delete(5,head)
# link_list_display(head)            
             
def inset_before(target,head):
    if head == None:
        return 0
    
    if head.data==target:
        i = input("Enter Input : ")
        node=Node(i)
        node.next=head
        return node
        
    if head.next.data==target:
       i = input("Enter Input : ")
       node=Node(i)
       node.next=head.next
       head.next=node
       return head
       
inset_before(3,head)
link_list_display(head) 
