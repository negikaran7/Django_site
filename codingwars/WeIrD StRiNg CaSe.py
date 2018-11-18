def to_weird_case(s):
    s = list(s)
    s_even = list(letter.upper() for letter in s[::2])
    s[::2] = s_even
    weird = ''
    for char in s:
        weird += char
    return weird
