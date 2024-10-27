citations = [1,10,100,1000]
def solution(citations):
    array = []
    for j in range(len(citations)+1):
        cnt = 0
        for i in citations:
            if j<= i:
                cnt += 1
        if j <= cnt:
            array.append(cnt)
    print(len(array) - 1)
    return len(array)-1

solution(citations)

#Best Solution
def solution(citations):
    citations.sort(reverse=True)
    h_index = 0
    for i in range(len(citations)):
        if citations[i] >= i + 1:
            h_index = i + 1
        else:
            break
    return h_index
