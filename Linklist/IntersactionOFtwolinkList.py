def Brut(head):
       if headA is None or headB is None:
            return None
        currentA = headA
        currentB = headB
        hashA,hashB = [],[]
        while currentA or currentB:
            if currentA is not None:
                if currentA in hashB:
                    return currentA
                hashA.append(currentA)
                currentA = currentA.next

            if currentB is not None:
                if currentB in hashA:
                    return currentB
                hashB.append(currentB)
                currentB = currentB.next
        return None

def Optimal(head):
        if headA is None or headB is None:
             return None
        
        currentA,currentB = headA, headB
        countA,countB = 0,0
        while currentA:
            
            countA+=1
            currentA = currentA.next
        
        while currentB:
            countB+=1
            currentB = currentB.next
        distance = abs(countA-countB)
        currentA = headA
        currentB = headB
        if countB >countA:
            while countB != countA:
                countB -=1
                currentB = currentB.next
        else :
            while countA != countB:
                countA -=1
                currentA = currentA.next
        while currentA and currentB:
            if currentA == currentB:
                return currentA
            currentA = currentA.next
            currentB = currentB.next
        return None
