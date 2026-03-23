class Solution:
    def isAnagram(self, s: str,t:str) -> bool:
        if len(s) != len(t):
            return False
        my_dict = dict()
        l = len(s)
        for i in range(l):
            my_dict[s[i]] = my_dict.get(s[i],0) +1
            my_dict[t[i]] = my_dict.get(t[i],0) -1
        for value in my_dict.values():
            if value != 0:
                return False
        return True            

s = "anagram"
t = "nagaram"
obj = Solution()
print(obj.isAnagram(s,t))
print(obj.isAnagram("car","rat"))
char = "a"
r = char*3
print(char+r)