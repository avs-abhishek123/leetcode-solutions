m =3
n=7
# m =3
# n=2

# 1st solution is that we can use math module
# print(math.comb(m+n-2,m-1))

# 2nd solution is dynamic programming solution
if m ==1 and n==1:
    print(1)
dp =[1]*n
for i in range(1,m):
    for j in range(1,n):
        dp[j]+=dp[j-1]
print(dp[n-1])