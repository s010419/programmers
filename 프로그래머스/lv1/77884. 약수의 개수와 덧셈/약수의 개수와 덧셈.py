def solution(left, right):
    answer = []
    sorted_num = list(range(left, right+1))
    for i in range(left, right+1):
        number = 0
        for j in range(1,i+1):         
            if i % j == 0:
                number += 1
        answer.append(number)
    num = []
    for i in range(right-left+1):
        if answer[i] % 2 == 0:
            num.append(sorted_num[i])
        else:
            num.append(sorted_num[i]*(-1))
    return sum(num)