T = int(input())
for tc in range(1, T + 1):
    n = int(input())            # n : 해빈이 의상 수
    cloth_dict = {}
    for _ in range(n):
        cloth_name, cloth_type = input().split()
        cloth_dict.setdefault(cloth_type, 1)
        cloth_dict[cloth_type] += 1
    total_sum = 1
    for value in cloth_dict.values():
        total_sum *= value
    print(total_sum - 1)