cnt = 0
def dfs(numbers, target, current, idx):
    global cnt
    if idx == len(numbers):
        # 끝까지 도착했을 때 목표 숫자랑 일치하면 cnt + 1
        if current == target:
            cnt += 1
        return
    dfs(numbers, target, current + numbers[idx], idx + 1)
    dfs(numbers, target, current - numbers[idx], idx + 1)


def solution(numbers, target):
    dfs(numbers, target, 0, 0)
    return cnt
