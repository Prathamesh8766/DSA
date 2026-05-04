def easy():
    food = int(input("Enter the total Number of food:"))
    max_meal = int(input("Enter Maximum Number Meals:"))
    initialTast = {}
    decreaseTast= {}
    for i in range(1,food+1):
        initialTast[i] = [int(input("Enter Total Tast point:")),1]
    for i in range(1,food +1):
        decreaseTast[i] = int(input("Enter Decrease Tast point:"))
    
    def findMax(max_meal, initialTast, decreaseTast):
        max_tast_point = 0
        while max_meal>0:
            max_key = max(initialTast, key = lambda k: initialTast[k][0])
            
            max_tast = initialTast[max_key][0]
            max_tast_point += max_tast

            decrease = decreaseTast[max_key]
            initialTast[max_key][0] -= decrease 
            initialTast[max_key][1]+=1
            max_meal -= 1
        return max_tast_point
    return findMax(max_meal,initialTast,decreaseTast)
print(easy())

def medium():
    size = int(input("Enter Size:"))
    k = int((input("Enter K:")))
    arr = []
    for i in range(size):
        a.append(int(input("Enter Element:")))
    i = 0, j = 1
    while k > 0:
        a[i],a[j] = a[j],a[i]
        i+=1
        j+=1
        k-= 1
