def openOrSenior(data):
    # Hmmm.. Where to start?
    rec = []
    for d in data:
        if d[0] >= 55 and d[1] > 7:
            rec.append("Senior")
        else:
            rec.append("Open")
    return rec


# def openOrSenior(data):
#     # Hmmm.. Where to start?
#     return ['Senior' if d[0] >= 55 and d[1] > 7 else 'Open' for d in data]
