from collections import deque
from linkListCreationAndOprations import LinkList
def evenOdd():
        even = deque()
        odd = deque()
        flag = 1
        current = head
        while current:
            if flag == 1:
                odd.append(current.val)
                flag = 0
            else:
                flag = 1
                even.append(current.val)
            current = current.next
        print(odd,even)
        current = head
        while odd:
            current.val = odd.popleft()
            current = current.next
        while even:
            current.val = even.popleft()
            current = current.next
        return head

def optimal(head):
    e = head.next
    eh = e
    o = head
    while e and e.next:
        o.next = o.next.next
        e.next = e.next.next
        o = o.next
        e = e.next
    o.next = eh
    return head

l2 = LinkList()
l2.createLinkList()
l2.displayLinkList()
l2.head= optimal(l2.head)
l2.displayLinkList()