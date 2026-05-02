# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
from collections import deque
def oddeven(head):
        even = deque()
        odd = deque()
        current = head
        while current:
            if current.val %2 ==0:
                even.append(current.val)
            else :
                odd.append(current.val)
        if currem.val %2 ==0:
            start = even
            end = odd
        else: 
            start = odd
            end = even
        current = head
        while start :
            current.val = start.popleft()
            current = current.next
        while end:
            current.val= edd.popleft()
            current =current.next 
        return head
