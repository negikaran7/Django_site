# The web is built with HTML strings like "<i>Yay</i>" which draws Yay as italic text.
# In this example, the "i" tag makes <i> and </i> which surround the word "Yay".
# Given tag and word strings, create the HTML string with tags around the word, e.g. "<i>Yay</i>".


# make_tags('i', 'Yay') → '<i>Yay</i>'
# make_tags('i', 'Hello') → '<i>Hello</i>'
# make_tags('cite', 'Yay') → '<cite>Yay</cite>'

# method 1
def make_tags1(tag, word):
    return('<{0}>{1}</{0}>'.format(tag, word))
print(make_tags1("title", "karan"))

# method 2
def make_tags2(tag, word):
    return (f'<{tag}>{word}</{tag}>')

print(make_tags2("i", "karan"))