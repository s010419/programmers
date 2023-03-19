def solution(x):
    list_x = sum(list(map(int,str(x))))
    if x % list_x == 0:
        return True
    else:
        return False