
def decimalToBinary(num):
    ans=0
    pow=1
    if num ==0:
        return 0
    while num > 0:
        rem = num%2
        num= num // 2  
        ans = ans + rem*pow

        pow =  pow*10
    return ans

print(decimalToBinary(66))    

def binaryToDecimal(num):
    ans=0
    pow=1
    if num == 0:
        return 0
    while num>0:
        rem = num % 10
        num = num // 10
        ans = ans + rem*pow
        pow = pow * 2

    return ans

print(binaryToDecimal(1000010))    