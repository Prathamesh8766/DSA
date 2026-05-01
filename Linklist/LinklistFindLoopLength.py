
from linkListCreationAndOprations import Node
def fingLoopLen(head):
    hash = {}
    curr = head
    time = 1
    while curr:
        
        if curr in hash:
            return time - hash[curr]
        hash[curr] = time
        time= time +1
        curr = curr.next
    return None 

def findLoopLenTortoizHare(head):

    fast = head
    slow = head
    while fast and fast.next:
        fast =fast.next.next
        slow = slow.next
        if slow ==  fast:
            count = 1
            fast = fast.next
            while fast != slow:
                fast = fast.next
                count +=1
            return count
        
    return None
l2 = Node(1)
l3 = Node(2)
l4 = Node(4)
l5 = Node(5)
l6 = Node(6)
l7 = Node(7)
l8 = Node(8)
l9 = Node(9)
l10 = Node(10)
l11 = Node(11)

l2.next = l3
l3.next = l4
l4.next = l5
l5.next = l6
l6.next = l7
l7.next = l8
l8.next = l9
l9.next = l10
l10.next = l11

l11.next = l5

print(f"length is {fingLoopLen(l2)}")
print(findLoopLenTortoizHare(l2))