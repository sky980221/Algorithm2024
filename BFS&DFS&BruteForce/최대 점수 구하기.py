def dfs(v):
    if v == N:
        temtime = []
        temscore = []
        for i in range(N):
            if visited[i] == 1:
                temtime.append(ptime[i])
                temscore.append(pscore[i])
        if sum(temtime) <= M:
            result.append(sum(temscore))


    else:
        visited[v] = 1
        dfs(v + 1)
        visited[v] = 0
        dfs(v + 1)

if __name__ == "__main__":
    N, M = map(int, input().split())
    array = []
    visited = [0] * N
    global score
    pscore = []
    ptime = []
    result = []
    for i in range(N):
        a, b = (map(int, input().split()))
        pscore.append(a)
        ptime.append(b)
    dfs(0)
    print(max(result))



#Best solution
def DFS(L, sum, time):
    global res
    if time > m:
        return
    if L == n:
        if sum > res:
            res = sum
    else:
        DFS(L+1, sum+pv[L], time+pt[L])
        DFS(L+1, sum, time)

if __name__ == "__main__":
    n, m = map(int, input().split())
    pv = list()
    pt = list()
    for i in range(n):
        a, b = map(int, input().split())
        pv.append(a)
        pt.append(b)
    res = -2147000000
    DFS(0, 0 , 0)
    print(res)


# 부분 집합으로 고려하면 해결하기 편함.