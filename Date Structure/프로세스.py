priorities = [1, 1, 9, 1, 1, 1]
location = 0

def solution(priorities, location):
    answer = 0
    array=[]
    target = [priorities[location],location]
    print(target)
    for i in range(len(priorities)):
        array.append([priorities[i], i])
    print(array)
    print(max(array, key=lambda x: x[0])[0])
    while array:
        if array[0][0] != max(array, key=lambda x: x[0])[0]:
            tmp = array.pop(0)
            array.append(tmp)
        else:
            tmp = array.pop(0)
            answer += 1
            if tmp == target:
                print(answer)
                return answer
    print(answer)
    return answer


solution(priorities, location)