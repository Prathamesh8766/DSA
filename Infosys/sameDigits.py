def sameDigit():
    m=int(input())
    for b in range(2,m):
        digits = []
        tep =m
        while tep>0:
            digits.append(tep%b)
            tep =tep //b
        
        if len(set(digits)) == 1:
            return b
print(sameDigit())