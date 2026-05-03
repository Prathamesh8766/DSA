   def isPalindrome(head) :
        # curr = head
        # s=""
        # while curr:
        #     s=s+f"{curr.val}"
        #     curr =curr.next
        # if s == s[::-1]:
        #     return True
        # else: return False
        fast = head
        slow = head
        while fast and  fast.next:
            fast = fast.next.next
            slow = slow.next
        def reverse(head):
            if head == None or head.next == None:
                return head
            new_head = reverse(head.next)
            front = head.next
            front.next = head
            head.next = None
            return new_head

      
        new_head = reverse(slow)
        
        print(new_head.val)
        current = head
        while new_head:
            if current.val != new_head.val:
                return False
            current = current.next
            new_head = new_head.next
        return True


        