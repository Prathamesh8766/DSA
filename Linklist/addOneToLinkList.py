from linkListCreationAndOprations import Node, LinkList
def addOne(head):
    if head.next is None:
        head.data += 1
        if head.data > 9:
            head.data = 0
            newNode = Node(data=1)
            newNode.next = head
            return newNode
        return head

    def reverse(head):
        current = head
        pre = None
        while current:
            front = current.next
            current.next = pre 
            pre = current
            current = front
        return pre
    
    head = reverse(head)

    current = head
    carry = 1   

    while current:
        num = current.data + carry

        current.data = num % 10
        carry = num // 10
        if carry == 0:
            break
        if current.next is None:
            current.next = Node(data=carry)
            carry = 0
            break
        current = current.next
    head = reverse(head)
    return head

l3= LinkList()
l3.createLinkList()
l3.displayLinkList()
l3.head = addOne(l3.head)
l3.displayLinkList()