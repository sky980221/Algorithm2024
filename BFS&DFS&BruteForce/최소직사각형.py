#Cannot Solve
def solution(sizes):
    w = []
    h = []
    for i in range(len(sizes)):
        if sizes[i][0] >= sizes[i][1]:
            w.append(sizes[i][0])
            h.append(sizes[i][1])
        else:
            h.append(sizes[i][0])
            w.append(sizes[i][1])

    return max(w) * max(h)

#w와 h의 의미를 무시하고 큰 놈을 w 배열에 넣고 작은  놈을 h에 넣은 뒤 각각의 max를 곱해준다.

#Best solution

#w, h중 큰 값을 모아서 그 중 큰 값과, w, h중 작은 값을 모아서 그 중 큰 값을 곱하면 간단하게 끝난다.
def solution(sizes):
    return max(max(x) for x in sizes) * max(min(x) for x in sizes)