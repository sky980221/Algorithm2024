# Wrong Answer (50.0/100)
def solution(n, lost, reserve):
    answer = n
    for i in lost:
        if i - 1 in reserve:
            reserve.remove(i - 1)
            continue
        elif i + 1 in reserve:
            reserve.remove(i + 1)
            continue
        else:
            answer = n - 1
            print(answer)
    return answer


# Best solution

def solution(n, lost, reserve):
    reserve_set = set(reserve) - set(lost)
    lost_set = set(lost) - set(reserve)

    for r in reserve_set:
        if r - 1 in lost_set:
            lost_set.remove(r - 1)
        elif r + 1 in lost_set:
            lost_set.remove(r + 1)

    return n - len(lost_set)

# set을 이용해서 여벌 체육복을 가져온 학생이 체육복을 도난당한 케이스를 제거
# 여벌 옷을 가져온 학생 루프 돌면서 앞 뒤로 빌려줄 애가 있는지 확인
# 나는 반대로 안 가져온 애를 돌렸는데, reserve를 돌았어야 함.
# 학생수 - 결국 끝까지 체육복이 없는 학생 = return