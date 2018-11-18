# def namelist(names):
    # namelist = [name['name'] for name in names]  #list comprehension  
#     if len(namelist) <= 1:
#         return ''.join(namelist)
#     else:
#         lastTwo = ' & '.join(namelist[-2:])
#         first = [n + ',' for n in namelist[:-2]]
#         first.append(lastTwo)
#         return ' '.join(first)

def namelist(names):
    names = [ hash["name"] for hash in names ]
    output = names[:-2]
    output.append(" & ".join(names[-2:]))
    return ", ".join(output)

print(namelist([ {'name': 'Bart'}, {'name': 'Lisa'}, {'name': 'Maggie'} ]))
