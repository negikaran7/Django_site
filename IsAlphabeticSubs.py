'''function to check all substrings'''


def get_all_substrings(input_string):
    length = len(input_string)
    return [input_string[i:j+1] for i in range(length) for j in range(i, length)]


sub = (get_all_substrings(input()))

'''list to show all substring with length greater than 2'''
d = []
for s in range(0, len(sub)):
    if len(sub[s]) >= 2:
        d.append(sub[s])
# print(d)

'''count all substrings in alphabetical order'''
count = 0
for subs in d:
    if subs == ''.join(sorted(subs)):
        count += 1
        print(subs)
print(count)

'''count all subs in alphabetical order i.e. ab, bc, rst. no gaps in the sequence'''
