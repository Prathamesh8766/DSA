def pattern2(n):
    for i in range(n):
        for j in range(n-i-1):
            print(" ", end="")
        for j in range(((2 * i + 1))):    
            print("*", end="")
        for j in range(n-i-1):
            print(" ", end="")
        print()            

def pattern1(n):
    for i in range(n):
        for j in range(i):
            print(" ", end="")
        for j in range((2 * n - (2 * i + 1))):    
            print("*", end="")
        for j in range(i):
            print(" ", end="")
        print()  
       
def pattern3(n):
    pattern2(n)
    pattern1(n)

pattern3(4)

def pattern4(n):
    for i in range(1, 2 * n):
        if i <= n:
            print("*" * i)
        else:
            print("*" * (2 * n - i))
pattern4(4)
def pattern5(n):
    for i in range(1, n):
        start = i % 2
        for j in range(i):
            print(start, end="")
            start = 1 - start
        print()
pattern5(5)  

def pattern6(n):
    for i in range(n+1):
        for j in range(1, i + 1):
            print(j, end="")

        for j in range((2 * n - (2 * i + 1))):
            print(" ", end="")
        for j in range(i, 0, -1):
            print(j, end="")

        print()


pattern6(5)

def pattern7(n):
    start = 1
    for i in range(1, n+1):
        for j in range(i):
            print(start, end=" ")
            start+=1
        print()
pattern7(5)  

def pattern5(n):
    for i in range(1, n+1):
        start = ord("A")
        for j in range(i):
            print(chr(start), end="")
            start += 1
        print()
pattern5(5)

def pattern8(n):
    for i in range(1, n+1):
        start = ord("A")
        for j in range(n+1 - i):
            print(chr(start), end="")
            start += 1
        print()
pattern8(5)

def pattern8(n):
    for i in range(n):
        ch = chr(ord("A") + i)
        for j in range(n-i):
            print(ch, end="")
        print()
pattern8(5)

def pattern10(n):
    for i in range(n):

        for j in range(n - i - 1):
            print(" ", end="")

        ch = ord("A")
        for j in range(2 * i + 1):
            print(chr(ch), end="")
            if j < i:
                ch += 1
            else:
                ch -= 1
     
        for j in range(n - i - 1):
            print(" ", end="")
        print()
pattern10(5)
def pattern11(n):
    for i in range(n, 0, -1):
        print("*" * i, end="")
        print(" " * (2 * (n - i)), end="")
        print("*" * i)
pattern11(5)
def pattern12(n):
    for i in range(1, n + 1):
        print("*" * i, end="")
        print(" " * (2 * (n - i)), end="")
        print("*" * i)
pattern12(5)
