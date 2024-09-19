#My solution
def solution(array, commands):
    answer = []
    subAnser = []
    for i in range(len(commands)):
        subAnswer = sorted(array[commands[i][0]-1:commands[i][1]])
        answer.append(subAnswer[commands[i][2]-1])
    return answer

#Best Solution

def solution(array, commands):
    answer = []

    for i in commands:
        ary = array[i[0] - 1: i[1]]  # 문제에서 주어진 크기만큼 자르기
        ary.sort()  # sort 함수로 정렬
        answer.append(ary[i[2] - 1])  # k 번째 값 집어넣기

    return answer

def solution(array, commands):
    return [sorted(array[i-1:j])[k-1] for i,j,k in commands]

# array[ ] 안에 넣음으로써 배열로 만들 수 있음.
# for i,j,k in commands 를 이용하면 굳이 이중 배열을 이용하여 복잡하게 하지 않아도 됨.
# range(len())에 너무 의존하지 말자.