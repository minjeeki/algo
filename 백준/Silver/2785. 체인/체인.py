N = int(input())
chains = list(map(int, input().split()))
cnt = 0
chains.sort(reverse=True)
len_chain = len(chains)
next_idx = 1
erase_idx = len_chain - 1
cnt = 0
while next_idx < len_chain and chains[next_idx] != 0:
    if chains[erase_idx] == 0:
        erase_idx -= 1
    chains[erase_idx] -= 1
    next_idx += 1
    cnt += 1
    # print(chains, next_idx)
print(cnt)