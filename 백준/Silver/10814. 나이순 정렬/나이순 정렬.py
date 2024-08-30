N = int(input())
age_dict = {}
for _ in range(N):
    age, name = input().split()
    age_dict.setdefault(int(age), [])
    age_dict[int(age)].append(name)
key_sorted = sorted(age_dict.keys())
for key in key_sorted:
    for name_item in age_dict[key]:
        print(key, name_item)