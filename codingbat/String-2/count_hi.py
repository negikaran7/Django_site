def count_hi(str):
    count = 0
    for i in range(len(str)-1):
        if str[i:i+2] == 'hi':
            count += 1
        # elif str[i:i+2] == 'HI':
        #     count += 1
        # elif str[i:i+2] == 'hI':
        #     count += 1
        # elif str[i:i+2] == 'Hi':
        #     count += 1
    return count
