from linkListCreationAndOprations import LinkList, Node



def addTwoNumbers( l1, l2):

        currentA = l1
        currentB = l2

        l3 = Node(0)
        temp = l3

        carry = 0

        while currentA or currentB:

            if currentA is not None and currentB is not None:

                num = currentA.data + currentB.data + carry

                carry = num // 10

                node = Node()
                node.data = num % 10

                temp.next = node
                temp = temp.next

                currentA = currentA.next
                currentB = currentB.next

            elif currentA is not None:

                num = currentA.data + carry

                carry = num // 10

                node = Node()
                node.data = num % 10

                temp.next = node
                temp = temp.next

                currentA = currentA.next

            elif currentB is not None:

                num = currentB.data + carry

                carry = num // 10

                node = Node()
                node.data = num % 10

                temp.next = node
                temp = temp.next

                currentB = currentB.next

        if carry > 0:
            node = Node()
            node.data = carry
            temp.next = node

        return l3.next

l1 =  LinkList()
l1.createLinkList()
l2 = LinkList()
l2.createLinkList()
l3=addTwoNumbers(l1.head,l2.head)
