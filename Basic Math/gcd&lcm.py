def gcd(a,b):
    if a==b:
        print(a)
        return
    n=abs(b-a)
    factor=[]
    i=1
    while i*i<=n:
        if a%i==0 and b%i==0:
            factor.append(i)
        i+=1    

    factor.sort()
    print(factor)
    print(f"{a},{b} is {factor[-1]} and i is {i}")
    return

gcd(2,6)
gcd(420,1782)
gcd(36,48)
gcd(13,11)
# proversion
def gcd(a, b):
    if a == b:
        return a

    n = abs(b - a)
    max_gcd = 1

    for i in range(1, int(n**0.5) + 1):
        if a % i == 0 and b % i == 0:
            max_gcd = max(max_gcd, i)
        
        j = n // i
        if a % j == 0 and b % j == 0:
            max_gcd = max(max_gcd, j)

    return max_gcd


def backtrack(i,n):
        if i>n:
            return
        backtrack(i+1,n)
        print(i)

backtrack(0,3)