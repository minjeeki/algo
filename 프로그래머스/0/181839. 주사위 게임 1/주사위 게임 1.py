def solution(a, b):
    a_is_odd = False if a % 2 == 0 else True
    b_is_odd = False if b % 2 == 0 else True
    if a_is_odd and b_is_odd:
        answer = a ** 2 + b ** 2
    elif a_is_odd == False and b_is_odd == False:
        answer = abs(a - b)
    else:
        answer = 2 * (a + b)
    return answer