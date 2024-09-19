# My solution
def solution(arr):
    answer = []
    for i in arr:
        if len(answer) == 0:
            answer.append(i)
        else:
            if i != answer[-1]:
                answer.append(i)
    return answer

# Best solution
def solution(arr):
    answer = []
    for i in arr:
        if [i] != answer[-1:]:
            answer.append(i)
    return answer

    # answer[-1:]를 이용하면 answer가 비어 있는지 여부를 따로 확인하지 않고, answer가 비어 있으면 answer[-1:]은 빈 리스트 []를 반환합니다.