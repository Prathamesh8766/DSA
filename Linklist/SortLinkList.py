from linkListCreationAndOprations import LinkList
from linkListCreationAndOprations import Node
from collections import deque
def BrutSortList(head):
        current = head
        l = deque()
        while current:
            l.append(current.data)
            current = current.next
        l = deque(sorted(l))
        print(l)
        current = head
        while current:
            current.data = l.popleft()
            current = current.next
        return head

def OptimalSortList(head) :
        
        def findMidle(head):
            slow = head
            fast = head.next
            while fast and fast.next:
                slow = slow.next
                fast = fast.next.next
            return slow
        def mergeSort(head):
            if head is None or head.next is None:
                return head
            midle =  findMidle(head)
            lefthead = head
            righthead = midle.next
            midle.next = None

            left =mergeSort(lefthead)
            right =mergeSort(righthead)

            dummy = Node(data = 0)
            temp = dummy
            while left is not None and right is not None:
                if left.data < right.data:
                    temp.next = left
                    left = left.next
                else:
                    temp.next = right
                    right = right.next
                temp = temp.next
            
            if left:
                temp.next = left
            if right:
                temp.next = right
            return dummy.next
        
        return mergeSort(head)

l3= LinkList()
l3.createLinkList()
l3.displayLinkList()
l3.head = BrutSortList(l3.head)
l3.displayLinkList()