# solution
def solution(numbers):
    numbers = [str(i) for i in numbers]
    numbers.sort(key=lambda x: x * 3, reverse=True)
    numbers = str(int(''.join(numbers)))
    return numbers
