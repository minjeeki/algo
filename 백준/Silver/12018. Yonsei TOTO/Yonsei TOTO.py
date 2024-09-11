n, m = map(int, input().split())                # 과목수 & 초기 마일리지
subject_max = []
for ni in range(n):
    p, l = map(int, input().split())            # 신청인원 & 수강인원
    mileages = list(map(int, input().split()))
    if p < l:
        subject_max.append(1)
    else:
        mileages.sort(reverse=True)
        subject_max.append(mileages[l - 1])
subject_max.sort()
cur_sum = 0
cnt = 0
for i in range(n):
    if cur_sum + subject_max[i] <= m:
        cur_sum += subject_max[i]
        cnt += 1
    else:
        break
print(cnt)