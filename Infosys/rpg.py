def rpg():
    numMoster = int(input())
    a = []
    e = int(input())
    defeated = 0
    for i in range(numMoster):
        l = [int(input())]
        a.append(l)
    for i in range(numMoster):
        a[i].append(int(input()))
    
    a.sort(key=lambda x:x[0])

    for i in a:
        if i[0] <= e:
            e+=i[1]
            defeated+=1
        else: break
    return defeated
        
print(rpg())