from linkListCreationAndOprations import LinkList
from collections import deque


def reverseSingleLinklistUsingStake(head):
    current = head
    stack = deque()
    while current:
        stack.append(current.data)
        current = current.next
    current = head
    while current:
        current.data = stack.pop()
        current = current.next
    return head

def reverseSingleLinklistUsingOptimal(head):
    current = head
    pre = None
    while current != None:
        front = current.next
        current.next = pre
        pre = current
        current = front
    return pre

def reverseSingleLinklistUsingRecursion(head):
    if head == None or head.next == None:
        return head
    new_head = reverseSingleLinklistUsingRecursion(head.next)
    front = head.next
    front.next = head
    head.next = None
    return new_head


l2 = LinkList()
l2.createLinkList()
l2.head = reverseSingleLinklistUsingStake(l2.head)
l2.displayLinkList()
l2.head = reverseSingleLinklistUsingOptimal(l2.head)
l2.displayLinkList()
l2.head = reverseSingleLinklistUsingRecursion(l2.head)
l2.displayLinkList()