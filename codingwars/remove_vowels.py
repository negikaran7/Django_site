def disemvowel(string):
    vowels = ('a', 'e', 'i', 'o', 'u','A','E','I','O','U')
    for x in string:
        if x in vowels:
            string =string.replace(x, "")
            
    return string

print(disemvowel("This website is for losers LOL!"))
# Ths wbst s fr lsrs LL!
# Ths wbst s fr lsrs LOL!