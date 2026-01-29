def powerOfTwo(num):
    if num > 0 and (num & (num - 1)) == 0:
        return True
    else:
        return False
    
print(powerOfTwo(6))    