n = int(input())
marks = [[input(), float(input())] for _ in range(n)]
scores = sorted({s[1] for s in marks})
result = sorted(s[0] for s in marks if s[1] == scores[1])
print('\n'.join(result))