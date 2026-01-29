a= { "b":3,"c":1 } 
b={"t":7,"j":8}
c={"o":1,"z":3}

def sort_dic(a,reverse):
    return dict(sorted(a.items(),key=lambda item:item[1],reverse=reverse))

print(sort_dic(a,False))

def check_is_exsistance(d,k):
    return k in d

print(check_is_exsistance(a,"c"))


def concantinate_dic(*dict):
    new_d={}

    for d in dict:
        new_d.update(d)

    return new_d

print(concantinate_dic(a,b,c))

def create_dict(b):
    return {i : i**3 for i in range(1,b+1)}
print(create_dict(7))


def sum_multiply(a):
    total_sum=0
    product=1
    for i in a.values():
        total_sum=total_sum+i
        product=product*i

    return f"sum = {total_sum} , product ={product}"
print(sum_multiply(a))    



def map_list_to_dic(a,b,d=None):
    
    if d is None:
        d={}     
    if not a or not b:
        return d    
    else:
        d[a[0]] = b[0]

        return map_list_to_dic(a[1:],b[1:],d)    

print(map_list_to_dic([1,"4"],[1,1]))


def max_min(a):
    val=a.values()
    return f"max: {max(val)} , min {min(val)}"
print(max_min(c))

def recusive_sum(a):
    if not a:
        return 0

    l1=list(a.items())
    curent_key,curent_val=l1[0]
    return curent_val+recusive_sum(dict(l1[1:]))
    
print(recusive_sum({"a":1,'b':2,"u":4}))    

res=1
for i in range(2):
    res=res * (4-i)
    res= res//(i+1)
print(res)    


ans=1
print(1,end=" ")
r=6
for i in range(1,6):
    ans = ans * (r-i)
    ans = ans // (i)
    print(ans,end=" ")