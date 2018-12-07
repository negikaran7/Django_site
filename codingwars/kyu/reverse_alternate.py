def reverse_alternate(string):
    words=string.split(" ")
    new_words=[]
    for i in range(len(words)):
        w=words[i]
        new_words.append(w) if i==0 or i%2==0 else new_words.append(w[::-1])
    return ' '.join(map(str, new_words))

print(reverse_alternate("karan singh negi hello how are you"))