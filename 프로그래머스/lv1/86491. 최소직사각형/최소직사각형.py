def solution(sizes):
    for i in range(len(sizes)):
        if sizes[i][0] < sizes[i][1]:
            sizes[i][0], sizes[i][1] = sizes[i][1], sizes[i][0]
            
    sizes0_list = []
    sizes1_list = []
    
    for i in sizes:
        sizes0_list.append(i[0])
    for i in sizes:
        sizes1_list.append(i[1])
    return max(sizes0_list)*max(sizes1_list)