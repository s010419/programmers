def solution(arr):
    answer = sorted(arr)
    arr.remove(answer[0])
    if arr == []:
        return [-1]
    return arr