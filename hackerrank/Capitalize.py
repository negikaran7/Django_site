def solve(s):
    cap = []
    sl = s.split(' ')
    for w in sl:
        if len(w) == 0:
            cap.append('')
        else:
            cap.append(w[0].upper() + w[1:])
    return ' '.join(cap)
