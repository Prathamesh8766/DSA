# # info = {"key":2,"hgv":9,
# #         "learn":"code",
# #         "age":34,
# #         "is":True,
# #         "marks":23,
# #         "hobbies":["read","ksa"],
# #         "sub":("skjc",76)}

# # print(type(info))
# # print(len(info))
# # print(info["hobbies"][0].title())
# # print(info["learn"].startswith("p"))
# # print(info.pop("key"))
# # print(info)
# # print(info.popitem())
# # print(info)
# # print(info.setdefault("asjk","g"))
# # print(info["hgv"])
# # print(info.get("hgv"))

# # #set(immutable,unorderd)
# # print("SET" \
# # " ")

# # p=set([6,45,"hg"])
# # print(p)
# # set1={4547,87,90,436,(7),True,}
# # set={"jh",436,87,90}
# # union=set1|set
# # intersection=set1&set
# # diff=set1-set
# # print(diff)
# # diff=set-set1
# # print(diff)
# # print(intersection)
# # print(set.add("89"))
# # set.add(90)
# # set.add("jhv")
# # #set.add("jhv","jhv")  TypeError: set.add() takes exactly one argument (2 given)
# # print(set.remove("89"))

# # print(set.discard(67))

# # """x = input()
# # y = True
# # while y is True:

# #         x_in = int(x)
# #         if x_in in range(1, 100):
# #             y = False
# #         else:
# #             x = input()"""

# # x=int(input("Table of "))
# # y=int(input("from "))
# # z=int(input("till "))

# # for i in range(y,z+1):
# #     print(x*i)


    
# # class Student:
# #     def __init__(self):
# #         self.name = "Zaheer"
# #         self.secondName = "prathmesh"
# #         self.thirdName = "Aditya"

# #     def getName(self):
# #         return self.name+ " " + self.secondName


# # obj = Student() 
# # def example_kwargs(**kwargs):
# #     for key, value in kwargs.items():
# #         print(f"{key} = {value}")

# # example_kwargs(a=1, b=2, c=3)
# # # Output:
# # # a = 1
# # # b = 2


# # print(obj.getName())
# # # 


# # def example_args(*args):
# #     for arg in args:
# #         print(arg)

# # example_args(1, 2, 3)
# # # Output:
# # # 1
# # # 2
# # # # 3
# # def reverse_string(s):
# #     reversed_str = ''
# #     for char in s:
# #         reversed_str = char + reversed_str
# #     return reversed_str


# # # Get user input
# # user_input = str(input("Enter a string to reverse: "))
# # reversed_result = reverse_string(user_input)
# # print("Reversed string:", reversed_result)


# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# node=TreeNode(3) 

# if node.left:
#     print("ok")
# else:
#     print("not ok")    



# stack=[1] 
# stack.append(2) 
# print(stack.pop())
a=4

def fibonacci(a):
    if a == 0:
        return 0
    elif a == 1:
        return 1
    else:
        return fibonacci(a-1) + fibonacci(a-2)
    
print(fibonacci(a))
# total=0
# for i in range(0,a+1):
#     total=total+i
# print(total)    