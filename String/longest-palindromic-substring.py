def longestPalindrome(s):
        if len(s) == 1: return s
        start , end = 0,0
        def func(s,left,rigth):

            while left >= 0 and rigth < len(s) and s[rigth] == s[left]:
                rigth+= 1
                left -= 1
            return rigth - left - 1
        
        for i in range(len(s)):
            odd = func(s, i, i)
            even = func(s, i, i + 1)
            max_len = max(odd, even)
            
            if max_len > end - start:
                start = i - (max_len - 1) // 2
                end = i + max_len // 2
        return s[start:end+1]