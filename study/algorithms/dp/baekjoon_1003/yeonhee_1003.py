import sys
input = sys.stdin.readline

# 31256kb,	40ms
def finbonacci(n):
    dp[0] = [1,0]
    dp[1] = [0,1]

    for i in range(2, n+1):
        if dp[i][0] > -1:
            continue
        dp[i][0] = dp[i-1][0] + dp[i-2][0]
        dp[i][1] = dp[i-1][1] + dp[i-2][1]
    
    print(str(dp[n][0]) + " " + str(dp[n][1]))

if "__main__" == __name__:
    tc = int(input())

    # dp리스트
    # [a,b] a 위치에는 0이 출력되는 갯수
    #       b 위치에는 1이 출력되는 갯수
    dp = [[-1,-1] for i in range(41)]
    for _ in range(tc):
        n = int(input())
        finbonacci(n)

