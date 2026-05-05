def removeNumbersothatNumberisgreatest():
    string = input()
    num = input()
    last_position = -1

    for i in range(len(string)):
        
        if string[i] == num:
            last_position = i
            if i < len(string) - 1 and string[i] < string[i + 1]:
                break

    if last_position == -1:
        last_position = len(string) - 1
        
    if last_position == -1: return string

    return string[:last_position]+string[last_position+1:]

print(removeNumbersothatNumberisgreatest())