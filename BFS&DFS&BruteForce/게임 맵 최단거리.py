from collections import deque

def solution(maps):
    # 시작점을 (0, 0)으로 설정하고, 종료점을 (len(maps)-1, len(maps[0])-1)으로 설정
    return BFS(0, 0, len(maps[0]) - 1, len(maps) - 1, maps)

def BFS(start_x, start_y, end_x, end_y, maps):
    dx = [-1, 1, 0, 0]  # 좌우 이동
    dy = [0, 0, -1, 1]  # 상하 이동
    queue = deque([(start_x, start_y, 1)])  # 시작점, 거리 1로 초기화
    visited = set([(start_x, start_y)])  # 방문 기록

    while queue:
        x, y, dist = queue.popleft()

        # 목표 지점에 도달했으면 거리 반환
        if x == end_x and y == end_y:
            return dist

        # 상하좌우로 이동
        for i in range(4):
            nx = x + dx[i]  # x축 이동
            ny = y + dy[i]  # y축 이동

            # 지도 범위 안에 있는지 확인
            if 0 <= nx < len(maps[0]) and 0 <= ny < len(maps):
                # 이동 가능한 경로(1)인지 확인하고 방문하지 않은 경우 이동
                if (nx, ny) not in visited:
                    if maps[ny][nx] == 1:
                        queue.append((nx, ny, dist + 1))
                        visited.add((nx, ny))

    return -1  # 도달할 수 없는 경우
