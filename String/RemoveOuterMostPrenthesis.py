# def function(s):
#             flag = 0
#             result = []
#             start = 0
#             for i in range(len(s)):
#                 if s[i] == "(" :
#                     flag += 1
#                 else: flag -= 1
#                 if flag == 0 :
#                     result.append(s[start+1 : i])
#                     start = i+1
#             result = "".join(result)
#             return result
# s= "(()())((()))"       
# print(function(s))

s = "the sky is blue"
arr= s.split()
print(arr)
l = len(arr) -1
for i in range((l // 2) + 1):
    arr[i], arr[l - i] = arr[l - i], arr[i]

print(arr ) 