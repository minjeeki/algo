N, M = map(int, input().split())
site_dict = {}
for _ in range(N):
    site, password = input().split()
    site_dict[site] = password
for _ in range(M):
    print(site_dict[input()])