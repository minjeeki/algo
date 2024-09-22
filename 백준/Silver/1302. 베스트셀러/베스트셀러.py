N = int(input())
books = {}
for _ in range(N):
    title = input()
    books.setdefault(title, 0)
    books[title] += 1
max_cnt = 0
max_title = []
for key, value in books.items():
    if value == max_cnt:
        max_cnt = value
        max_title.append(key)
    elif value > max_cnt:
        max_cnt = value
        max_title = [key]
print(sorted(max_title)[0])