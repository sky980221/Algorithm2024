s = input()
cnt = 0
arr = [-1]
answer = []
for i in s:
    if arr[-1] == i:
        cnt += 1
    else:
        cnt = 1
    arr.append(i)
    if cnt == 3:
        answer.append(str(arr[-1]) * 3)
        cnt = 0
if len(answer) == 0:
    print("-1")
else:
    answer.sort()
    print(str(int(answer[-1])))


#Best Solution
def solution(s):
    biggest = -1  # 멋쟁이 숫자가 없으면 -1을 반환할 기본값
    for i in range(len(s) - 2):  # 길이가 3인 부분 문자열 탐색
        if s[i] == s[i + 1] == s[i + 2]:  # 세 자리가 모두 같은지 확인
            biggest = max(biggest, int(s[i] * 3))  # 가장 큰 숫자 저장
    return biggest  # 결과 반환
