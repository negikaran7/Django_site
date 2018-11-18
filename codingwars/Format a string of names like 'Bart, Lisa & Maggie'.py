def namelist(names):
    new_list=[]
    for i in range(len(names)):
        if i>=len(names)-2:
            new_list.append(names[i]["name"])
        else:
            new_list.append(names[i]["name"])

    return ' '.join(map(str, new_list))

print(namelist([ {'name': 'Bart'}, {'name': 'Lisa'}, {'name': 'Maggie'} ]))
