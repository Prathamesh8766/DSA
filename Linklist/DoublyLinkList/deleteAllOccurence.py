from doubleLinklistandOperation import DoubleLinklist, Node

def deleteAllOccurrence(head, target):
    curr = head
    while curr:
        if head is not None and head.data == target:
            head = head.next
            if head is not None:
                head.pre = None
            curr = head
        elif curr.data == target:
            curr.pre.next = curr.next
            if curr.next is not None:
                curr.next.pre = curr.pre
            curr = curr.next
        else:
            curr = curr.next
    return head

l1 = DoubleLinklist()
l1.creationOfDoubleLinklist()
l1.display()
l1.head = deleteAllOccurrence(l1.head, "1")
l1.display()