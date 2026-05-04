from linkListCreationAndOprations import Node, LinkList
def Brut(head):
    if head is None or head.next is  None:
        return head
    count0, count1, count2 = 0,0,0
    current = head
    while current :
        if current.data == 0:
            count0+=1
        elif current.data == 1:
            count1+=1
        else:
            count2+=1
        current = current.next
    current = head
    while count0>0:
        current.data = 0
        count0-=1
        current = current.next
    while count1>0:
        current.data = 1
        count1-=1
        current = current.next
    while count2>0:
        current.data = 2
        count2-=1
        current = current.next
    return head

def OptmimalSort012(head):
    if head is None or head.next is  None:
        return head
    
    zerodummy = Node(data = -1)
    onedummy = Node(data = -1)
    twodummy = Node(data = -1)
    zero = zerodummy
    one = onedummy
    two = twodummy
    current = head
    while current:
        nextNode = current.next
        current.next = None
        if current.data == 0:
            zero.next = current
            zero = zero.next
        if current.data == 1:
            one.next = current
            one = one.next
        if current.data == 2:
            two.next = current
            two = two.next
        
        current = nextNode

        if zerodummy.next is not None:
            head = zerodummy.next
            zero.next = onedummy.next if onedummy.next else twodummy.next
        elif onedummy.next is not None:
            head = onedummy.next
        else:
            head = twodummy.next

        if onedummy.next is not None:
            one.next = twodummy.next

    return head

l4 = LinkList()
l4.createLinkList()
l4.displayLinkList()
l4.head = OptmimalSort012(l4.head)

l4.displayLinkList()