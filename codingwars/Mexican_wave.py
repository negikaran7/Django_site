def wave(str):
    # Code here
    new_wave = []
    for i in range(0, len(str)):
        if str[i]==" ":
            pass
        else:
            new_wave.append(str[0:i]+str[i].upper()+str[i+1:])
    return new_wave
print(wave(input()))