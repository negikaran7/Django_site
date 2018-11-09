def make_chocolate(small, big, goal):
    numb = goal / 5
    if big >= numb:
        if small >= goal - numb*5:
            return goal - numb*5
    if big < numb:
        if small >= goal - big*5:
            return goal - big*5
    return -1
