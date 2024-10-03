def solution(n, computers):
    answer = 0
    visited = [False for _ in range(n)]
    for com in range(n):
        if visited[com] == False:
            DFS(n, computers, com, visited)
            answer += 1
    return answer

#computers = [[1,1,0], [1,1,0], [0,0,1]] n = 3
#com == 0
def DFS(n, computers, com, visited):
    visited[com] = True
    for i in range(n):
        if i != com and computers[com][i] and visited[i] == False:
            DFS(n, computers, i, visited)

#자기 자신이 아니고, 이전 노드(com)와 현재 노드(i)가 연결된 노드이며, 현재 노드가 방문하지 않은 노드라면 방문하고, 현재 노드(i)에 대한 DFS를 계속 진행