#Bottom-up 방식
#점화식이라고 이해하면 편함. 1일때를 구하고, 2일때는 1에다가 n을 곱하면 커지고 이런식...
N = int(input())

dp= [0]*(N+1)
dp[1] = 1
dp[2] = 2

for i in range(3,N+1):
    dp[i] = dp[i-1] + dp[i-2]

print(dp[N])

#Top-down 방식 (memoization)
#미리 한 번 구해놓은 것을 기록해서, 다음에 동일한 것이 호출 되었을 때, cut edge함.
def DP(len):
    #dy[len]값이 있으면 이미 구한 값이니까 else문에서 가지 뻗지말고 바로 리턴해라
    if dy[len]>0:
        return dy[len]
    if len == 1 or len == 2:
        return len
    else:
        dy[len] = DP(len-1) + DP(len-2)
        return dy[len]

if __name__=="__main__":
    n = int(input())
    dy = [0]*(n+1)
    print(DP(n))