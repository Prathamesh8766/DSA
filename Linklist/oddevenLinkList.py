def evenOdd()
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