def beautySum(s) :
        if len(s) == 1: return 0
        beauty = []
        for i in range(len(s)):
            my_dict = {}
            for j in range(i,len(s)):
                if s[j] not in my_dict:
                    my_dict[s[j]] = 1
                else:
                    my_dict[s[j]] += 1
                max_fre = max(my_dict.values())
                min_fre = min(my_dict.values())

                beauty.append(max_fre - min_fre)
        return sum(beauty)