def solution(n, m):
    answer = [1]
    n,m = max(n,m), min(n,m)
    for i in range(1,n+1):
        if n%i == 0 and m%i == 0:
            if i > answer[0]:
                answer[0] = i
    if m%n == 0:
        answer.append(m)
    else:
        answer.append(m*n/answer[0])
    return answer