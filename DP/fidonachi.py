def fid(n):
    if n == 0:
        return 0
    if n==1:
        return 0
    if n==2:
        return 1
    return fid(n-1)+fid(n-2)

print(fid(9))


# using dp wit memoization

def dp_fib(n):
    
    dp = [0, 1] + [None] * (n - 1)

    def helper(n):

        if n==0:
          return 0
        if n==1:
            return 1
 
        if dp[n] != None:
            
            return dp[n]
           
        dp[n] = helper(n-1)+helper(n-2)


        return dp[n]
    return helper(n)

print(dp_fib(8))    


#using tabulation

def dp_tebulation(n):

    dp=[None]*(n+1)
    dp[0]=1
    dp[1]=1
    dp[2]=1

    for i in range(3,n+1):
        dp[i]=dp[i-1]+dp[i-2]

    return dp[n]
print(dp_tebulation(8))    