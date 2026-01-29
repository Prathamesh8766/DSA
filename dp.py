call={}
diary=[-1]*(50+1)
def fid_with(n):
    if n<1:
        return 1
    if diary[n]!=-1:
        return diary[n]
    if n not in call:
        call[n]=1
    else:
        call[n]+=1
    fid1=fid_with(n-1)        
    fid2=fid_with(n-2)
    diary[n-1]=fid1
    diary[n-2]=fid2

    ans=fid1+fid2
    diary[n]=ans
    return ans

print(fid_with(11))
print(call)



def fib_with_tabulation(n):
    if n<=1:
        return 1
    dp=[0]*(n+1)
    print(dp)
    dp[0]=0
    dp[1]=1
    for i in range(2,n+1):
        dp[i]=dp[i-1]+dp[i-2]
    return dp[n]    

print(fib_with_tabulation(11))

