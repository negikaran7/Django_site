# Given a non-empty string like "Code" return a string like "CCoCodCode".


# string_splosion('Code') → 'CCoCodCode'
# string_splosion('abc') → 'aababc'
# string_splosion('ab') → 'aab'

def string_splosion(str):
    str1 = ""
    for i in range(0, len(str)+1):
        str1 = str1+str[0:i]
        i += 1
    return str1
