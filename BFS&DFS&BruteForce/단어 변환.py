from collections import deque


def solution(begin, target, words):
    answer = 0
    queue = deque([begin])
    visited = set([begin])

    while queue:
        # 현재 레벨(단계)에 있는 모든 단어를 처리한 후 answer를 증가
        for _ in range(len(queue)):  # 현재 큐에 있는 모든 단어를 탐색
            curr_node = queue.popleft()
            if curr_node == target:
                return answer
            for next_node in words:
                if next_node not in visited:
                    if diff(curr_node, next_node) == True:
                        visited.add(next_node)
                        queue.append(next_node)
        answer += 1
    return 0


def diff(a, b):
    cnt = 0
    arr1 = [i for i in a]
    arr2 = [j for j in b]
    for i in range(len(arr1)):
        if arr1[i] == arr2[i]:
            cnt += 1
    if cnt == len(a) - 1:
        return True
    else:
        return False

