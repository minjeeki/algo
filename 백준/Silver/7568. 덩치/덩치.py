N = int(input())
biggy_lst = [0] * N
grade_lst = [0] * N
for i in range(N):
    person_info = list(map(int, input().split()))
    biggy_lst[i] = person_info
for p1_idx in range(N):
    p1_grade = 1
    for p2_idx in range(N):
        if biggy_lst[p1_idx][0] < biggy_lst[p2_idx][0] and \
            biggy_lst[p1_idx][1] < biggy_lst[p2_idx][1]:
            p1_grade += 1
    grade_lst[p1_idx] = p1_grade
print(*grade_lst)