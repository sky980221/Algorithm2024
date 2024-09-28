# numbers = [i + 1 for i in range(N)]
# result = []
# visited = []
# array = []
#
# def dfs(numbers, idx):
#     if idx <= len(numbers)-1:
#         for i in range(len(numbers)):
#             if numbers[i] not in array:
#                 array.append(numbers[i])
#             else:
#                 array.append(numbers[i+1])
#         if array in result:
#             dfs(numbers, idx + 1)
#         else:
#             result.append(array)
#             print(result)
#             dfs(numbers, idx)
#     return
# dfs(numbers, 0)
# 그냥 절망적이다....
def DFS(v):
    if v == n+1:
        for i in range(1,n+1):
            if visited[i] == 1:
                print(i, end=' ')
        print()
    else:
        visited[v]=1
        DFS(v+1)
        visited[v]=0
        DFS(v+1)
if __name__=="__main__":
    n=int(input())
    visited = [0]*(n+1)
    DFS(1)
