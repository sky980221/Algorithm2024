
def DFS(v):
    global found
    if found:
        return
    if v == N:
        sum1 = []
        sum2 = []
        for i in range(N):
            if visited[i] == 1:
                sum1.append(arr[i])
        sum2 = sum(arr) - sum(sum1)
        if sum(sum1) == sum2:
            print("YES")
            found = True
    else:
        visited[v] = 1
        DFS(v+1)
        visited[v] = 0
        DFS(v+1)

if __name__=="__main__":
    N = int(input())
    arr = list(map(int, input().split(' ')))
    visited = [0]*(N)
    found = False
    DFS(0)
    if found == False:
        print("NO")



#Best soulution
def DFS(L, sum):
    if sum > total // 2:
        return
    if L == n:
        if sum == total - sum:
            print("YES")
            sys.exit(0)
    else:
        DFS(L + 1, sum + a[L])
        DFS(L + 1, sum)

if __name__ == "__main__":
    n = int(input())
    a = list(map(int, input().split()))
    total = sum(a)
    DFS(0, 0)
    print("NO")

#굳이 전역변수를 사용하지말고 Main 함수에서 해결하는 것도 좋은 방법임.