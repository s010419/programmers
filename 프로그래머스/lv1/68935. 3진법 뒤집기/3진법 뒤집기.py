def solution(n):
    answer = 0
    rev_base = ''
    while n > 0:
        n, mod = divmod(n, 3)
        rev_base += str(mod)
    list_rev = list(rev_base[::-1])
    for i in range(len(list_rev)):
        answer += int(list_rev[i])*3**i
    return answer