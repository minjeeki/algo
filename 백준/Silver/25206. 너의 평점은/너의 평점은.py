N = 20
alpha = 'FDCBA'
bonus = {'+': 0.5, '0': 0}
sum_hakjum = 0
class_score = 0
for _ in range(N):
    grade = input().split()
    if grade[2][0] == 'P':
        continue
    hakjum = float(grade[1])
    subject_score = alpha.index(grade[2][0])
    if len(grade[2]) == 2 and grade[2][1] == '+':
        subject_score += 0.5
    sum_hakjum += hakjum
    class_score += (hakjum * subject_score)
print(f'{class_score/sum_hakjum:.6f}')