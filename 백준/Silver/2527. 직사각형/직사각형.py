for _ in range(4):
    x1, y1, p1, q1, x2, y2, p2, q2 = list(map(int, input().split()))

    # relation = d
    if p2 < x1 or p1 < x2 or q2 < y1 or q1 < y2:
        relation = 'd'
    # relation = c
    elif y1 == q2 or q1 == y2:
        if x1 == p2 or p1 == x2:
            relation = 'c'
        else:
            relation = 'b'
    # relation = b
    elif p1 == x2 or x1 == p2:
            relation = 'b'
    # relation = a
    else:
          relation = 'a'
    print(relation)