def josephus_survivor(n, k):
    v = 0
    for i in range(1, n + 1):
        v = (v + k) % i
        print(f'after {i} iteration v is {v}')
    return v + 1
josephus_survivor(7, 3)
