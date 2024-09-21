# bottom up

def solution(N, number):
    if number == N:
        return 1
    answer = -1
    array = [set() for i in range(8)]
    for i in range(len(array)):
        array[i].add(int(str(N) * (i + 1)))

    for i in range(1, 8):
        for j in range(i):
            for op1 in array[j]:
                for op2 in array[i - j - 1]:
                    array[i].add(op1 + op2)
                    array[i].add(op1 - op2)
                    array[i].add(op1 * op2)
                    if op2 != 0:
                        array[i].add(op1 // op2)
        if number in array[i]:
            answer = i + 1
            break
    return answer