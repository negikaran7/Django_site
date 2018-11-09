def cat_dog(str):
    count_c = 0
    count_d = 0
    for i in range(len(str)-1):
        if str[i:i+3] == 'cat':
            count_c += 1
        elif str[i:i+3] == 'dog':
            count_d += 1
    return count_c == count_d
