def solution(my_string, alp):
    my_lst = list(my_string)
    for idx in range(len(my_lst)):
        if my_lst[idx] == alp:
            my_lst[idx] = alp.upper()
    answer = ''.join(my_lst)
    return answer