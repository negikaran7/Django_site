def same_structure_as(original,other):
    struct1 = check(original, "")
    struct2 = check(other, "")
    return struct1 == struct2



def check(arr, current):
    if type(arr) is list:
        current += '['
        for a in arr:
            if type(a) is list:
                current += check(a, current)
            else:
                current += 'x'
            
        current += ']'
    return current

print(same_structure_as([[1,2],2],[[1,2],2]))