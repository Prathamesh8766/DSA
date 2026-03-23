def arange(s):
    s="tree"
    l = len(s)
    buckets=[[] for _ in range(l+1)]
    freq_dict = dict()
    for char in s:
                freq_dict[char] = freq_dict.get(char,0) + 1
    for key,value in freq_dict.items():
                buckets[value].append(key)
    result = []
    for i in range(len(buckets) - 1, 0, -1):
        for char in buckets[i]:
            result.append(char * i)
            
    return ("".join(result)    ,buckets, freq_dict)
print(arange("tree"))