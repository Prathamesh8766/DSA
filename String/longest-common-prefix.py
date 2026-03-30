def longestCommonPrefix(strs):
    
        if len(strs) == 1: return strs[0]
        result = ""
        helper = strs[0]
        strs = strs[1:]

        for i in strs:
            j =0
            if len(helper) > len(i):
                helper , i = i, helper
            while j < len(helper):
                if helper[j] != i[j]:
                    helper = helper[0:j]
                    break
                j+=1
                
        
        return helper