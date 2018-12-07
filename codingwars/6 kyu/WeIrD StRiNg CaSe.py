def to_weird_case(string):
    word_list = list(string.split(' '))
    new_word_list = []
    for word in word_list:
        charac_list = []
        for index in range(len(word)):
            if index % 2 == 0:
                charac_list.append(word[index].upper())
            else:
                charac_list.append(word[index].lower())
        new_word_list.append(''.join(charac_list))
    return ' '.join(new_word_list)

print(to_weird_case("HELP"))
