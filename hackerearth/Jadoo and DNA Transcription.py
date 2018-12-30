dna=input()
mapping = {'A': 'U',
           'C': 'G',
           'T': 'A',
           'G': 'C'}
try:
    result = ''.join([mapping.get(ch) for ch in dna])
except TypeError:
    print("Invalid Input")
else:
    print(result)
